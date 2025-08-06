import React from 'react';
import QuantityControls from './common/QuantityControls.jsx';
import styled from 'styled-components';

const CardItem = styled.div`
  border: 1px solid #dee2e6;
  border-radius: 0.75rem;
  padding: 1rem;
  margin-bottom: 1rem;
  background-color: #fff;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
`;

const Title = styled.h6`
  font-weight: bold;
  margin-bottom: 0.1rem;
`;

const GridContainer = styled.div`
  display: grid;
  grid-template-columns: 1fr 120px 80px;
  align-items: center;
  gap: 1rem;

  .producto-nombre {
    overflow: hidden;
  }

  .producto-cantidad {
    justify-self: end;
  }
  
  .producto-precio {
    justify-self: end;
    font-size: 1.1rem;
    font-weight: bold;
    color: #e4231f;
    white-space: nowrap;
  }

  /* Media Query para pantallas móviles */
  @media (max-width: 768px) {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }
`;

const MobileControlsWrapper = styled.div`
  display: none; // Oculto por defecto en desktop
  @media (max-width: 768px) {
    display: flex; // Visible solo en móvil
    justify-content: space-between;
    align-items: center;
    width: 100%;
  }
`;

const DesktopControlsWrapper = styled.div`
  display: contents; // Muestra los hijos directamente sin un contenedor extra
  @media (max-width: 768px) {
    display: none; // Oculto en móvil
  }
`;

function CartItem({ item, onIncrement, onDecrement }) {
  const formatPrice = (price) => {
    const numericPrice = parseFloat(price);
    return new Intl.NumberFormat('es-AR', {
      style: 'currency',
      currency: 'ARS',
      minimumFractionDigits: 0,
      maximumFractionDigits: 2
    }).format(numericPrice);
  };

  return (
    <CardItem>
      <GridContainer>
        <div className="producto-nombre">
          <Title>{item.nombre}</Title>
        </div>

        {/* Versión para escritorio: elementos separados para la grid */}
        <DesktopControlsWrapper>
          <div className="producto-cantidad">
            <QuantityControls
              quantity={item.cantidad}
              onIncrement={() => onIncrement(item)}
              onDecrement={() => onDecrement(item.id)}
            />
          </div>
          <div className="producto-precio">
            <span>{formatPrice(parseFloat(item.precio) * item.cantidad)}</span>
          </div>
        </DesktopControlsWrapper>

        {/* Versión para móvil: contenedor agrupado */}
        <MobileControlsWrapper>
          <QuantityControls
            quantity={item.cantidad}
            onIncrement={() => onIncrement(item)}
            onDecrement={() => onDecrement(item.id)}
          />
          <div className="producto-precio">
            <span>{formatPrice(parseFloat(item.precio) * item.cantidad)}</span>
          </div>
        </MobileControlsWrapper>
      </GridContainer>
    </CardItem>
  );
}

export default CartItem;
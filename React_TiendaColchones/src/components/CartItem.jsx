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

const InfoSection = styled.div`
  flex: 1;
  display: flex;
  flex-direction: column;
`;

const HeaderRow = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

const Title = styled.h6`
  font-weight: bold;
  margin-bottom: 0.1rem;
`;

const Price = styled.span`
  font-size: 1.1rem;
  color: #e4231f;
  font-weight: bold;
`;

const QuantityWrapper = styled.div`
  margin-top: 0.5rem;
`;

const GridContainer = styled.div`
  display: grid;
  grid-template-columns: 1fr 120px 80px; /* Fijamos ancho para botones y precio */
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
        <div className="producto-cantidad">
            <QuantityControls
            quantity={item.cantidad}
            onIncrement={() => onIncrement(item)}
            onDecrement={() => onDecrement(item.id)}
            />
        </div>
        <div className="producto-precio">
            <Price>{formatPrice(parseFloat(item.precio) * item.cantidad)}</Price>
        </div>
        </GridContainer>
    </CardItem>
    );
}

export default CartItem;
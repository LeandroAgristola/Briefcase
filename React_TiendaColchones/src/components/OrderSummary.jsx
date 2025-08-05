// src/components/OrderSummary.jsx
import React from 'react';
import styled from 'styled-components';

const StyledOrderSummary = styled.div`
  border-top: 1px solid #dee2e6;
  padding-top: 1.5rem;
  margin-top: 1.5rem;
`;

const StyledTotal = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-weight: bold;
  font-size: 1.5rem;
  margin-bottom: 1rem;
`;

const StyledButtonContainer = styled.div`
  display: flex;
  gap: 1rem;
`;

function OrderSummary({ totalCompra, formatPrice, onConfirmPurchase, onClearCart }) {
  return (
    <StyledOrderSummary>
      <StyledTotal>
        <span>Total:</span>
        <span style={{ color: '#e4231f' }}>{formatPrice(totalCompra)}</span>
      </StyledTotal>
      <StyledButtonContainer>
        <button
          className="btn btn-dark btn-lg w-100"
          onClick={onConfirmPurchase}
        >
          Confirmar
        </button>
        <button
          className="btn btn-outline-secondary btn-lg w-100"
          onClick={onClearCart}
        >
          Vaciar Carrito
        </button>
      </StyledButtonContainer>
    </StyledOrderSummary>
  );
}

export default OrderSummary;
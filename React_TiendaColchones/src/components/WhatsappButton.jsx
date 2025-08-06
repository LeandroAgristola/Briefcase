// src/components/WhatsappButton.jsx

import React from 'react';
import styled from 'styled-components';
import { FaWhatsapp } from 'react-icons/fa';

// Estilo del botón usando styled-components
const StyledWhatsappButton = styled.a`
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: #25d366;
  color: #fff;
  font-size: 2rem;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  text-decoration: none;
  transition: transform 0.3s ease, background-color 0.3s ease;
  z-index: 1000;

  &:hover {
    transform: scale(1.1);
  }

  /* Media query para hacerlo responsivo en pantallas más pequeñas */
  @media (max-width: 768px) {
    bottom: 20px;
    right: 20px;
    width: 50px;
    height: 50px;
    font-size: 1.8rem;
  }
`;

// Componente de React que usa el estilo
const WhatsappButton = () => {
  return (
    <StyledWhatsappButton
      href="https://api.whatsapp.com/send?phone=+5491187654321"
      target="_blank"
      rel="noopener noreferrer"
      aria-label="Chatea con nosotros por WhatsApp"
    >
      <FaWhatsapp />
    </StyledWhatsappButton>
  );
};

export default WhatsappButton;
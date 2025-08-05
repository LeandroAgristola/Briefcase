import React, { useState } from 'react';
import { useCart } from '../context/CartContext.jsx';
import { toast } from 'react-toastify';
import { Modal, Button } from 'react-bootstrap';
import styled from 'styled-components';
import { Link } from 'react-router-dom';
import CartItem from './CartItem.jsx';
import OrderSummary from './OrderSummary.jsx';

const StyledProgressBar = styled.div`
  .progress-bar {
    background-color: #586875;
    transition: width 2s ease-in-out;
  }
`;

function Cart() {
  const { carrito, agregarAlCarrito, disminuirCantidad, vaciarCarrito } = useCart();
  const [isPurchasing, setIsPurchasing] = useState(false);
  const [purchaseCompleted, setPurchaseCompleted] = useState(false);
  const [showClearCartModal, setShowClearCartModal] = useState(false);

  const formatPrice = (price) => {
    const numericPrice = parseFloat(price);
    return new Intl.NumberFormat('es-AR', {
      style: 'currency',
      currency: 'ARS',
      minimumFractionDigits: 0,
      maximumFractionDigits: 2
    }).format(numericPrice);
  };

  const totalCompra = carrito.reduce((total, item) => total + (parseFloat(item.precio) * item.cantidad), 0);

  const handleShowClearCartModal = () => setShowClearCartModal(true);
  const handleCloseClearCartModal = () => setShowClearCartModal(false);
  const handleConfirmClearCart = () => {
    vaciarCarrito();
    handleCloseClearCartModal();
    toast.info('El carrito ha sido vaciado.');
    if (purchaseCompleted) setPurchaseCompleted(false);
  };

  const handleConfirmPurchase = () => {
    if (carrito.length === 0) {
      toast.error('Tu carrito está vacío. Agrega productos para confirmar la compra.');
      return;
    }
    setIsPurchasing(true);
    toast.info('Procesando tu compra...');

    setTimeout(() => {
      setIsPurchasing(false);
      setPurchaseCompleted(true);
      vaciarCarrito();
      toast.success('¡Compra realizada con éxito! Gracias por tu pedido.');
    }, 2000);
  };

  // Componente para el carrito vacío (extraído para mayor legibilidad)
  const EmptyCart = () => (
    <div className="container py-5">
      <div className="card shadow-sm p-4">
        <div className="card-body text-center">
          <h2 className="card-title mb-3">Tu carrito está vacío.</h2>
          <p className="card-text lead">¡Parece que aún no has agregado ningún producto!</p>
          <Link to="/productos" className="btn btn-dark mt-3">Explorar productos</Link>
        </div>
      </div>
    </div>
  );

  if (purchaseCompleted) {
    return (
      <div className="container py-5 text-center">
        <h2 className="mb-4">¡Compra Realizada con Éxito!</h2>
        <p className="lead">Gracias por tu pedido. En breve recibirás un correo con los detalles de tu compra.</p>
        <p className="mt-4">
          <Link to="/productos" className="btn btn-dark btn-lg">Seguir comprando</Link>
        </p>
      </div>
    );
  }

  if (carrito.length === 0 && !purchaseCompleted) {
    return <EmptyCart />;
  }

  return (
    <div className="container py-5">
      <h2 className="mb-4">Tu Carrito de Compras</h2>

      <div className="row">
        <div className="col-md-8">
          <ul className="list-unstyled mb-3">
            {carrito.map((item) => (
              <CartItem
                key={item.id}
                item={item}
                onIncrement={agregarAlCarrito}
                onDecrement={disminuirCantidad}
              />
            ))}
          </ul>
        </div>

        <div className="col-md-4">
          {!isPurchasing && (
            <div className="card shadow-sm p-3" style={{borderRadius: '0.75rem' }}>
              <OrderSummary
                totalCompra={totalCompra}
                formatPrice={formatPrice}
                onConfirmPurchase={handleConfirmPurchase}
                onClearCart={handleShowClearCartModal}
              />
            </div>
          )}
        </div>
      </div>
        <Modal show={showClearCartModal} onHide={handleCloseClearCartModal} centered>
        <Modal.Header closeButton>
          <Modal.Title>Confirmar Vaciado de Carrito</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <p>¿Estás seguro de que quieres eliminar todos los productos de tu carrito?</p>
          <p className="fw-bold text-danger">Esta acción no se puede deshacer.</p>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleCloseClearCartModal}>
            Cancelar
          </Button>
          <Button variant="danger" onClick={handleConfirmClearCart}>
            Vaciar Carrito
          </Button>
        </Modal.Footer>
      </Modal>
    </div>
  );
}

export default Cart;
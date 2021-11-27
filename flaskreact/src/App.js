import React from "react";
import { ToastContainer, toast } from 'react-toastify';

class App extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      _id:'',
      nombre:'',
      precio:'',
      libros:[] // array para recoger los recursos del libro
    }
    this.handleChange = this.handleChange.bind(this);
    this.addlibro = this.addlibro.bind(this);
  }

  handleChange(e){
    const { name, value} = e.target;
    this.setState({
      [name]: value
    });
  }
  
  refrescarLibros(){
    const apiUrl = 'http://localhost:5600/Libros';
    fetch(apiUrl)
    .then((response) => response.json())
    .then((data) => {
      this.setState({libros:data});
      console.log(this.state.libros);
    })
  }
  // el metodo que se ejecuta al cargar este componente

  componentDidMount(){
    this.refrescarLibros();
  }

  addlibro(e){
    e.preventDefault();
    if (this.state._id){
      fetch(`http://localhost:5600/Libros/${this.state._id.$oid}`,{
        method:'PUT',
        body: JSON.stringify({
          nombre: this.state.name,
          precio: this.state.precio,
        }),
        headers:{
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        }
      })
      .then(res => res.json())
      .then(data => {
        this.setState({_id:'',nombre:'', precio:''});
        toast.success("Updated/Saved",{
          position: toast.POSITION.BOTTOM_RIGHT,
          autoClose:1000
        })
        this.refrescarLibros();
      });
      
    }
    else{
      fetch(`http://localhost:5600/Libros`,{
        method:'POST',
        body:JSON.stringify(this.state),
        headers:{
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        }
      })
      .then(res => res.json())
      .then(data => {
        this.setState({nombre:'',precio:''});
        toast.success("Updated/Saved",{
          position: toast.POSITION.BOTTOM_RIGHT,
          autoClose:1000
        })
        this.refrescarLibros();
      });
    }
  }

  deletelibri(_id){
    if(window.confirm('Está seguro de eliminar el Libro')){
      fetch(`http://localhost:5600/Libros/${_id}`,{
        method:'DELETE',
        headers:{
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        }
      })
      .then(res=>res.json())
      .then(data =>{
       toast.success("Producto borrado éxitosamente...",{
          position: toast.POSITION.TOP_LEFT,
          autoClose:2000
        })
        this.refrescarLibros();
      });
    }
  }

  editlibro(_id){
    fetch(`http://localhost:5600/Libros/${_id}`)
    .then(res => res.json())
    .then(data =>{
      this.setState({
        nombre:data.nombre,
        precio:data.precio,
        _id:data._id
      });
    });
  }

  render(){
    return (
      <div className="container">
        <h1 style={{color:'green'}}>Actualizacion de libros</h1>
        {/* Formulario*/}
        <form onSubmit={this.addlibro}>
          <div className="mb-3">
            <label htmlFor="name">Nombre</label>
            <input type="text" name="nombre" className="form-control" 
            onChange={this.handleChange} value={this.state.nombre}
            placeholder="Nombre" autoFocus
            ></input>

          </div>
          <div className="mb-3">
            <label htmlFor="name">Precio</label>
            <input type="number" name="precio" className="form-control" 
            onChange={this.handleChange} value={this.state.precio}
            placeholder="Precio"></input>

          </div>
          
          <button type="submit" className="btn btn-primary">Guardar</button>
        </form>
        {/* Fin formulario*/}
        <table className='table table-hover'>
          <thead>
            <tr>
              <th>Id</th>
              <th>Nombre</th>
              <th>Precio</th>
              <th>Accion</th>
            </tr>
          </thead>
          <tbody>
            {
              this.state.libros.map(libro =>{
                return(
                  <tr key={JSON.stringify(libro._id.$oid)}>
                    <td>{JSON.stringify(libro._id.$oid)}</td>
                    <td>{libro.nombre}</td>
                    <td>{libro.precio}</td>
                    <td>
                      <button onClick={()=>this.editlibro(libro._id.$oid)} className="btn btn-primary" style={{margin: '4px'}}>
                      Editar
                      </button>
                      <button onClick={()=>this.deletelibro(libro._id.$oid)} className="btn btn-danger" style={{margin: '4px'}}>
                      Eliminar
                      </button>
                    </td>
                  </tr>
                )
              })
            }
          </tbody>
        </table>

      </div>
    );
  }
}

export default App;

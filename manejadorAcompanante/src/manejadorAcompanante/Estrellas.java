package manejadorAcompanante;

public class Estrellas implements VOEstrellas{
	
	private long id;
	
	private String nombre;
	
	private String apellido;
	
	private String correo;
	
	public Estrellas (long id, String nombre, String apellido, String correo) {
		this.id = id;
		this.nombre = nombre;
		this.apellido = apellido;
		this.correo = correo;
	}

	public long getId() {
		return id;
	}

	public void setId(long id) {
		this.id = id;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getApellido() {
		return apellido;
	}

	public void setApellido(String apellido) {
		this.apellido = apellido;
	}

	public String getCorreo() {
		return correo;
	}

	public void setCorreo(String correo) {
		this.correo = correo;
	}
	
	public String toString() {
		return ( "ID: " + this.getId() + " - Nombre: " +
				this.getNombre() + " - Apellido: " + this.getApellido() + 
				" - Correo: " + this.getCorreo());
	}
	
}
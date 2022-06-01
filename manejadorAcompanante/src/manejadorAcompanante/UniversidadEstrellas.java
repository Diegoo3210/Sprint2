package manejadorAcompanante;

public class UniversidadEstrellas implements VOUniversidadEstrellas {
	
	private long estrellasID;
	
	private String universidad;
	
	private String carrera;

	public long getEstrellasID() {
		return estrellasID;
	}

	public void setEstrellasID(long estrellasID) {
		this.estrellasID = estrellasID;
	}

	public String getUniversidad() {
		return universidad;
	}

	public void setUniversidad(String universidad) {
		this.universidad = universidad;
	}

	public String getCarrera() {
		return carrera;
	}

	public void setCarrera(String carrera) {
		this.carrera = carrera;
	}
	
	public String toString() {
		return ( "ID: " + this.getEstrellasID() + " - " + "Universidad: " +
				this.getUniversidad() + " - " + "Carrera: " + this.getCarrera());
	}
	
}

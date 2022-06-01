package manejadorAcompanante;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

public class manejadorAcompanante {
	
	private moduloConsulta consulta;
	
	private long psicologoID;
	
	private String usuario;
	
	private String contrasena;
	
	public List<VOEstrellas> consultaEstrellas() {
		List<VOEstrellas> completa = consulta.getEstrellasPsicologo(this.psicologoID);
		return completa;
		
	}
	
	public void rolUsuario(String usuario, String contrasena) throws SQLException{
		
		try (ResultSet rta = consulta.getRolUsuario(usuario, contrasena)) {
			if(rta != null) {
				this.usuario = rta.getString(5);
				this.contrasena = rta.getString(6);
				this.psicologoID = rta.getInt(1);
			}
		}
        
    }
    
    public manejadorAcompanante(){
        this.consulta = new moduloConsulta(); 
    }

    public static void main(String args[]) throws SQLException{
        manejadorAcompanante companante = new manejadorAcompanante();
        
        /* PRUEBA DE QUE FUCIONA
        List<VOEstrellas> rta = consultaEstrellas();
        System.out.println("hola");
        for (int i = 0; i < rta.size(); i++) {
        	VOEstrellas x = rta.get(i);
        	System.out.println(x.toString());
        }
        */
    }
    
    
}

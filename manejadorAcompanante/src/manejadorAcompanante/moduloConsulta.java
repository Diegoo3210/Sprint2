package manejadorAcompanante;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class moduloConsulta {
	
	public List<VOEstrellas> getEstrellasPsicologo(long psicologoID) {
		List<VOEstrellas> rs = new ArrayList<VOEstrellas>();
		
		try {
            // step1 load the driver class
            Class.forName("oracle.jdbc.driver.OracleDriver");

            // step2 create the connection object
            Connection con = DriverManager.getConnection(
                    "jdbc:oracle:thin:@fn4.oracle.virtual.uniandes.edu.co:1521/prod", "ISIS2304C04202210", "dUGekGqCLbvu");

            // step3 create the statement object
            Statement stmt = con.createStatement();

            // step4 execute query
            ResultSet query = stmt.executeQuery(
            		"SELECT ESTRELLAS.ID, ESTRELLAS.NOMBRE, ESTRELLAS.APELLIDO, ESTRELLAS.CORREO\r\n"
            		+ "FROM PSICOLOGO, ESTRELLAS, ACOMPANAMIENTO\r\n"
            		+ "WHERE PSICOLOGO.ID = ACOMPANAMIENTO.PSICOLOGOID AND PSICOLOGOID = '" + psicologoID + "'");
            while (query.next()) {
            	Estrellas estrella = new Estrellas(query.getLong(1), query.getString(2), query.getString(3), query.getString(4));
            	VOEstrellas voEstrella = (VOEstrellas)estrella;
            	rs.add(voEstrella);
            }
            // step5 close the connection object
            con.close();

        } catch (Exception e) {
            System.out.println(e);
        }
		
		return rs;
    }
		
	
	public ResultSet getRolUsuario(String usuario, String contrasena) {
		ResultSet rs = null;
		try {
            // step1 load the driver class
            Class.forName("oracle.jdbc.driver.OracleDriver");

            // step2 create the connection object
            Connection con = DriverManager.getConnection(
                    "jdbc:oracle:thin:@fn4.oracle.virtual.uniandes.edu.co:1521/prod", "ISIS2304C04202210", "dUGekGqCLbvu");

            // step3 create the statement object
            Statement stmt = con.createStatement();

            // step4 execute query
            rs = stmt.executeQuery(
            		"SELECT * \r\n"
            		+ "FROM PSICOLOGO\r\n"
            		+ "WHERE USUARIO = '" + usuario + "' AND CONTRASENA = '" + contrasena + "';");
            
            // step5 close the connection object
            con.close(); 
            
        } catch (Exception e) {
            System.out.println(e);
        }
		
		return rs;

    }
	
    public moduloConsulta() {
    	
    }
	
}

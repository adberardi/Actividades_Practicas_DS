/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package client;

import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import remoteobject.Hola;

/**
 * Actividad RMI Unidad 7
 * @author adtony45 - Antonio Berardi
 */
public class Client {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws RemoteException, NotBoundException {
        // TODO code application logic here
        Registry reg = LocateRegistry.getRegistry("127.0.0.1", 1000);
        Hola h = (Hola) reg.lookup("objetoSaludar");
        System.out.println(h.saludar());
    }
}

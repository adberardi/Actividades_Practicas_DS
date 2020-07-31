/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package server;

import java.rmi.AlreadyBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import remoteobject.ImpleHola;

/**
 *
 * @author adtony45
 */
public class Server {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws RemoteException, AlreadyBoundException {
        // TODO code application logic here
        Registry reg = LocateRegistry.createRegistry(1000);
        reg.rebind("objetoSaludar", new ImpleHola());
        System.out.println("Servidor preparado!");
    }
}

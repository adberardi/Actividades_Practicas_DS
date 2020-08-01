/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package remoteobject;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

/**
 * Actividad RMI Unidad 7
 * @author adtony45 - Antonio Berardi
 */
public class ImpleHola extends UnicastRemoteObject implements Hola {
    
    public ImpleHola() throws RemoteException {
        super();
    }
    
    @Override
    public String saludar() throws RemoteException {
        return "Hola a todos!";
    }
    
}

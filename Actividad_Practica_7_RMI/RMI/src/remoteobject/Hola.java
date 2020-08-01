/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package remoteobject;

import java.rmi.Remote;
import java.rmi.RemoteException;

/**
 * Actividad RMI Unidad 7
 * @author adtony45 - Antonio Berardi
 */
public interface Hola extends Remote{
    public String saludar() throws RemoteException;
}

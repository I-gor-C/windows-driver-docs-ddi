---
UID: NS.ntddpcm._PCMCIA_SOCKET_INFORMATION
title: PCMCIA_SOCKET_INFORMATION
author: windows-driver-content
description: The PCMCIA_SOCKET_INFORMATION structure is used in conjunction with the IOCTL_SOCKET_INFORMATION request to retrieve socket configuration and state data.
old-location: pcmcia\pcmcia_socket_information.htm
old-project: PCMCIA
ms.assetid: 53881aca-e49c-43e9-b68e-b91a1868e3f5
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: PCMCIA_SOCKET_INFORMATION, PCMCIA_SOCKET_INFORMATION, *PPCMCIA_SOCKET_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddpcm.h
req.include-header: Ntddpcm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PCMCIA_SOCKET_INFORMATION
req.alt-loc: ntddpcm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# PCMCIA_SOCKET_INFORMATION structure



## -description
<p>The PCMCIA_SOCKET_INFORMATION structure is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537275">IOCTL_SOCKET_INFORMATION</a> request to retrieve socket configuration and state data. </p>


## -syntax

````
typedef struct _PCMCIA_SOCKET_INFORMATION {
  USHORT Socket;
  USHORT TupleCrc;
  UCHAR  Manufacturer[MANUFACTURER_NAME_LENGTH];
  UCHAR  Identifier[DEVICE_IDENTIFIER_LENGTH];
  UCHAR  DriverName[DRIVER_NAME_LENGTH];
  UCHAR  DeviceFunctionId;
  UCHAR  Reserved;
  UCHAR  CardInSocket;
  UCHAR  CardEnabled;
  ULONG  ControllerType;
} PCMCIA_SOCKET_INFORMATION, *PPCMCIA_SOCKET_INFORMATION;
````


## -struct-fields
<dl>

### -field Socket

<dd>
<p>Indicates the socket number. </p>
</dd>

### -field TupleCrc

<dd>
<p>Contains a 16-bit CRC that is concatenated with the PCMCIA prefix, the manufacturer-name string, the product-name string, and the instance value for the card to produce the device ID for a PC Card or CardBus card. For more information about PCMCIA device IDs, see <a href="devinst.identifiers_for_pcmcia_devices">Identifiers for PCMCIA Devices</a>. </p>
</dd>

### -field Manufacturer

<dd>
<p>Indicates the manufacturer of the PC Card or CardBus card. </p>
</dd>

### -field Identifier

<dd>
<p>Contains the device ID of the PC Card or CardBus card. </p>
</dd>

### -field DriverName

<dd>
<p>Contains the name of the PC Card or CardBus card device driver. </p>
</dd>

### -field DeviceFunctionId

<dd>
<p>Indicates the type of PC Card or CardBus card. This value can be one of the following.</p>
<table>
<tr>
<th>PC Card Type</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>PCCARD_TYPE_MULTIFUNCTION</p>
</td>
<td>
<p>Multifunction card.</p>
</td>
</tr>
<tr>
<td>
<p>PCCARD_TYPE_MEMORY</p>
</td>
<td>
<p>Memory card.</p>
</td>
</tr>
<tr>
<td>
<p>PCCARD_TYPE_SERIAL</p>
</td>
<td>
<p>Serial port card.</p>
</td>
</tr>
<tr>
<td>
<p>PCCARD_TYPE_PARALLEL</p>
</td>
<td>
<p>Parallel port card.</p>
</td>
</tr>
<tr>
<td>
<p>PCCARD_TYPE_ATA</p>
</td>
<td>
<p>Disk controller card. </p>
</td>
</tr>
<tr>
<td>
<p>PCCARD_TYPE_VIDEO</p>
</td>
<td>
<p>Video controller card. </p>
</td>
</tr>
<tr>
<td>
<p>PCCARD_TYPE_NETWORK</p>
</td>
<td>
<p>Network controller card. </p>
</td>
</tr>
<tr>
<td>
<p>PCCARD_TYPE_AIMS</p>
</td>
<td>
<p>Auto-increment mass storage card. </p>
</td>
</tr>
<tr>
<td>
<p>PCCARD_TYPE_SCSI_BRIDGE</p>
</td>
<td>
<p>SCSI bridge card. </p>
</td>
</tr>
<tr>
<td>
<p>PCCARD_TYPE_SECURITY</p>
</td>
<td>
<p>Security card. </p>
</td>
</tr>
<tr>
<td>
<p>PCCARD_TYPE_MULTIFUNCTION3</p>
</td>
<td>
<p>Multifunction 3.0 PC Card. </p>
</td>
</tr>
<tr>
<td>
<p>PCCARD_TYPE_FLASH_MEMORY</p>
</td>
<td>
<p>Flash memory card. </p>
</td>
</tr>
<tr>
<td>
<p>PCCARD_TYPE_MODEM</p>
</td>
<td>
<p>Modem card. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field Reserved

<dd>
<p>Reserved. </p>
</dd>

### -field CardInSocket

<dd>
<p>Indicates that there is a card present in the socket. </p>
</dd>

### -field CardEnabled

<dd>
<p>Indicates that the card is enabled. </p>
</dd>

### -field ControllerType

<dd>
<p>Indicates the controller type. Some common controller types are defined in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537600">PCMCIA_CONTROLLER_CLASS</a> enumeration. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddpcm.h (include Ntddpcm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537275">IOCTL_SOCKET_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [PCMCIA\buses]:%20PCMCIA_SOCKET_INFORMATION structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

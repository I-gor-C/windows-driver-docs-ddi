---
UID: NE.spb.SpbIoctl
title: SpbIoctl
author: windows-driver-content
description: Defines values to indicate the type I/O control request.
old-location: spb\spbioctl.htm
old-project: SPB
ms.assetid: 83260550-B364-4790-BDB5-5C6E5AD76A72
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: VENDOR_ATTR, VENDOR_ATTR, *PVENDOR_ATTR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: spb.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SpbIoctl
req.alt-loc: Spb.h
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
req.product: Windows 10 or later.
---

# SpbIoctl enumeration



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>Defines values to indicate the type I/O control request.</p>


## -syntax

````
typedef enum _SpbIoctl { 
  IOCTL_SPB_LOCK_CONTROLLER,
  IOCTL_SPB_UNLOCK_CONTROLLER,
  IOCTL_SPB_EXECUTE_SEQUENCE,
  IOCTL_SPB_LOCK_CONNECTION,
  IOCTL_SPB_UNLOCK_CONNECTION,
  IOCTL_SPB_FULL_DUPLEX
} SpbIoctl, *PSpbIoctl;
````


## -enum-fields
<dl>

### -field IOCTL_SPB_LOCK_CONTROLLER

<dd>
<p>The <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/spb/spb-ioctls">IOCTL_SPB_LOCK_CONTROLLER</a> control code is used by a client (peripheral driver) to lock the SPB controller. While the controller is locked, the client has exclusive use of the bus to access the specified target device for the lock.</p>
</dd>

### -field IOCTL_SPB_UNLOCK_CONTROLLER

<dd>
<p>The <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/spb/spb-ioctls">IOCTL_SPB_UNLOCK_CONTROLLER</a> I/O control code is used by a client (peripheral driver) to unlock the SPB controller. The client previously locked the controller to gain exclusive use of the bus to access a target device on the bus.</p>
</dd>

### -field IOCTL_SPB_EXECUTE_SEQUENCE

<dd>
<p>The <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/spb/spb-ioctls">IOCTL_SPB_EXECUTE_SEQUENCE</a> I/O control code enables a client (peripheral driver) of the SPB controller driver to perform a sequence of transfers (reads and writes) as a single, atomic operation with one I/O request. The designated device on the bus is the target for all transfers in the sequence.</p>
</dd>

### -field IOCTL_SPB_LOCK_CONNECTION

<dd>
<p>The <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/spb/spb-ioctls">IOCTL_SPB_LOCK_CONNECTION</a> control code is used by a client (peripheral driver) to acquire the connection lock on an SPB-connected target device that is shared with another client. While a client holds the connection lock,  this client has exclusive access to the device.</p>
</dd>

### -field IOCTL_SPB_UNLOCK_CONNECTION

<dd>
<p>The <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/spb/spb-ioctls">IOCTL_SPB_UNLOCK_CONNECTION</a> I/O control code is used by a client (peripheral driver) to release the connection lock on an SPB-connected target device that is shared with another client. The client previously sent an <a href="https://msdn.microsoft.com/library/windows/hardware/jj819324">IOCTL_SPB_LOCK_CONNECTION</a> request to acquire exclusive access to the device.</p>
</dd>

### -field IOCTL_SPB_FULL_DUPLEX

<dd>
<p>The <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/spb/spb-ioctls">IOCTL_SPB_FULL_DUPLEX</a> control code is used by a client (peripheral driver) to request a full-duplex I/O operation. Full-duplex I/O operations are supported by controllers for buses such as SPI that can simultaneously read and write data.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Spb.h</dt>
</dl>
</td>
</tr>
</table>
---
UID: NS.parallel._PARALLEL_1284_COMMAND
title: PARALLEL_1284_COMMAND
author: windows-driver-content
description: The PARALLEL_1284_COMMAND structure specifies information that a client uses to select and deselect an IEEE 1284.3 daisy-chain device or an IEEE 1284 end-of-chain device.
old-location: parports\parallel_1284_command.htm
old-project: parports
ms.assetid: 5b46253c-c111-4675-898e-78b81ecbddb8
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: PARALLEL_1284_COMMAND, PARALLEL_1284_COMMAND, *PPARALLEL_1284_COMMAND
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: parallel.h
req.include-header: Parallel.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PARALLEL_1284_COMMAND
req.alt-loc: parallel.h
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

# PARALLEL_1284_COMMAND structure



## -description
<p>The PARALLEL_1284_COMMAND structure specifies information that a client uses to select and deselect an IEEE 1284.3 daisy-chain device or an IEEE 1284 end-of-chain device.</p>


## -syntax

````
typedef struct _PARALLEL_1284_COMMAND {
  UCHAR ID;
  UCHAR Port;
  ULONG CommandFlags;
} PARALLEL_1284_COMMAND, *PPARALLEL_1284_COMMAND;
````


## -struct-fields
<dl>

### -field <b>ID</b>

<dd>
<p>Specifies the IEEE 1284.3 device ID.</p>
</dd>

### -field <b>Port</b>

<dd>
<p>Reserved (set to zero).</p>
</dd>

### -field <b>CommandFlags</b>

<dd>
<p>Specifies a bitwise OR of zero or more of the following flags:</p>
<p></p>
<dl>

### -field <a id="PAR_END_OF_CHAIN_DEVICE"></a><a id="par_end_of_chain_device"></a>PAR_END_OF_CHAIN_DEVICE

<dd>
<p>Specifies an end-of-chain device.</p>
</dd>

### -field <a id="PAR_HAVE_PORT_KEEP_PORT"></a><a id="par_have_port_keep_port"></a>PAR_HAVE_PORT_KEEP_PORT

<dd>
<p>Specifies that the client has the parallel port allocated, and makes a request to keep the port allocated.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The system-supplied function driver for parallel ports supports the simultaneous connection of zero to two IEEE 1284.3 daisy-chain devices and an IEEE 1284 end-of-chain device. In Windows XP, the parallel port function driver supports the simultaneous connection of zero to four IEEE 1284.3 daisy-chain devices and an IEEE 1284 end-of-chain device. The end-of-chain device must be an IEEE 1284 device, but does not have to be an IEEE 1284.3 device. </p>

<p>For more information, see <a href="https://msdn.microsoft.com/1a3ac1b1-9180-4b71-8740-70c6fbe9a885">Selecting and Deselecting an IEEE 1284 Device Attached to a ParallelPort</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Parallel.h (include Parallel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543987">IOCTL_INTERNAL_DESELECT_DEVICE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544052">IOCTL_INTERNAL_SELECT_DEVICE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544504">PPARALLEL_DESELECT_ROUTINE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544767">PPARALLEL_TRY_SELECT_ROUTINE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [parports\parports]:%20PARALLEL_1284_COMMAND structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

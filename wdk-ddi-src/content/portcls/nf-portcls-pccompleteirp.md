---
UID: NF.portcls.PcCompleteIrp
title: PcCompleteIrp function
author: windows-driver-content
description: The PcCompleteIrp function completes an IRP that was previously marked as pending.
old-location: audio\pccompleteirp.htm
old-project: audio
ms.assetid: fa0b36bf-0628-4136-9ca7-1d20823969ff
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: PcCompleteIrp
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: The PortCls system driver implements the PcCompleteIrp function in Microsoft Windows 98/Me and in Windows 2000 and later operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PcCompleteIrp
req.alt-loc: Portcls.lib,Portcls.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Portcls.lib
req.dll: 
req.irql: <=DISPATCH_LEVEL
---

# PcCompleteIrp function



## -description
The <b>PcCompleteIrp</b> function completes an IRP that was previously marked as pending.



## -syntax

````
NTSTATUS PcCompleteIrp(
  _In_ PDEVICE_OBJECT DeviceObject,
  _In_ PIRP           Irp,
  _In_ NTSTATUS       Status
);
````


## -parameters

### -param DeviceObject [in]

Pointer to the device object for the device. This parameter must point to a system structure of type <a href="kernel.device_object">DEVICE_OBJECT</a>.


### -param Irp [in]

Pointer to the <a href="kernel.irp">IRP</a> that is to be completed


### -param Status [in]

Specifies the status of the completed IRP. See the list of NTSTATUS values defined in header file ntstatus.h.


## -returns
<b>PcCompleteIrp</b> returns STATUS_SUCCESS if the call was successful. Otherwise, it returns an appropriate error code.


## -remarks
<b>PcCompleteIrp</b> is used when an IRP handler returns STATUS_PENDING and the IRP must later be completed. When the adapter driver finishes all processing of the IRP, it calls <b>PcCompleteIrp</b> to complete the IRP.

The IRP handler should not call this function. An adapter driver's IRP handler instead calls <a href="audio.pcdispatchirp">PcDispatchIrp</a> to pass the IRP to the PortCls system driver's IRP handler to perform all remaining processing of the IRP.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
The PortCls system driver implements the PcCompleteIrp function in Microsoft Windows 98/Me and in Windows 2000 and later operating systems.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Portcls.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;=DISPATCH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="audio.pcdispatchirp">PcDispatchIrp</a>
</dt>
<dt>
<a href="kernel.iocompleterequest">IoCompleteRequest</a>
</dt>
<dt>
<a href="kernel.device_object">DEVICE_OBJECT</a>
</dt>
<dt>
<a href="kernel.irp">IRP</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PcCompleteIrp function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


---
UID: NF.wmilib.WmiCompleteRequest
title: WmiCompleteRequest function
author: windows-driver-content
description: The WmiCompleteRequest routine indicates that a driver has finished processing a WMI request in a DpWmiXxx routine.
old-location: kernel\wmicompleterequest.htm
old-project: kernel
ms.assetid: c6377dcc-a83b-4766-b882-25d228a26efe
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: WmiCompleteRequest
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wmilib.h
req.include-header: Wmilib.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WmiCompleteRequest
req.alt-loc: Wmilib.lib,Wmilib.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wmilib.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WmiCompleteRequest function



## -description
The <b>WmiCompleteRequest</b> routine indicates that a driver has finished processing a WMI request in a <i>DpWmiXxx</i> routine.


## -syntax

````
NTSTATUS WmiCompleteRequest(
  _In_    PDEVICE_OBJECT DeviceObject,
  _Inout_ PIRP           Irp,
  _In_    NTSTATUS       Status,
  _In_    ULONG          BufferUsed,
  _In_    CCHAR          PriorityBoost 
);
````


## -parameters

### -param DeviceObject [in]

A pointer to the driver's <a href="kernel.device_object">DEVICE_OBJECT</a>.

### -param Irp [in, out]

A pointer to the IRP. 

### -param Status [in]

Specifies the status to return for the IRP. 

### -param BufferUsed [in]

Specifies the number of bytes needed in the buffer passed to the driver's <i>DpWmiXxx</i> routine. If the buffer is too small, the driver sets <i>Status</i> to STATUS_BUFFER_TOO_SMALL and sets <i>BufferUsed</i> to the number of bytes needed for the data to be returned. If the buffer passed is large enough, the driver sets <i>BufferUsed</i> to the number of bytes actually used. 

### -param PriorityBoost  [in]

Specifies a system-defined constant by which to increment the run-time priority of the original thread that requested the operation. WMI calls <a href="kernel.iocompleterequest">IoCompleteRequest</a> with <i>PriorityBoost</i> when it completes the IRP. See <b>IoCompleteRequest</b> for more information on <i>PriorityBoost</i>. 

## -returns
<b>WmiCompleteRequest</b> returns the value that was passed to it in the <i>Status</i> parameter unless <i>Status</i> was set to STATUS_BUFFER_TOO_SMALL.  If the driver set <i>Status</i> equal to STATUS_BUFFER_TOO_SMALL, <b>WmiCompleteRequest</b> builds a WNODE_TOO_SMALL structure and returns STATUS_SUCCESS. The return value from <b>WmiCompleteRequest</b> should be returned by the driver in its <i>DpWmiXxx</i> routine.

## -remarks
A driver calls <b>WmiCompleteRequest</b> from a <i>DpWmiXxx</i> routine after it finishes all other processing in that routine, or after the driver finishes all processing for a pending IRP. <b>WmiCompleteRequest</b> fills in a <b>WNODE_<i>XXX</i></b> with any data returned by the driver and calls <b>IoCompleteRequest</b> to complete the IRP.

A driver should always return the return value from <b>WmiCompleteRequest</b> in its <i>DpWmiXxx</i> routine.

A driver must not call <b>WmiCompleteRequest</b> from its <a href="kernel.dpwmiqueryreginfo">DpWmiQueryRegInfo</a> routine. 

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
Available starting with Windows 2000.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wmilib.h (include Wmilib.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Wmilib.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
&lt;= DISPATCH_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.dpwmiexecutemethod">DpWmiExecuteMethod</a>
</dt>
<dt>
<a href="kernel.dpwmifunctioncontrol">DpWmiFunctionControl</a>
</dt>
<dt>
<a href="kernel.dpwmiquerydatablock">DpWmiQueryDataBlock</a>
</dt>
<dt>
<a href="kernel.dpwmiqueryreginfo">DpWmiQueryReginfo</a>
</dt>
<dt>
<a href="kernel.dpwmisetdatablock">DpWmiSetDataBlock</a>
</dt>
<dt>
<a href="kernel.dpwmisetdataitem">DpWmiSetDataItem</a>
</dt>
<dt>
<a href="kernel.iocompleterequest">IoCompleteRequest</a>
</dt>
<dt>
<a href="kernel.wmisystemcontrol">WmiSystemControl</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20WmiCompleteRequest routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

---
UID: NF.mcd.ChangerError
title: ChangerError
author: windows-driver-content
description: ChangerError performs device-specific error handling.
old-location: storage\changererror.htm
old-project: storage
ms.assetid: e2196971-47ad-4ac4-a3e9-c8f7f6b05321
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ChangerError
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: mcd.h
req.include-header: Mcd.h, Ntddchgr.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ChangerError
req.alt-loc: mcd.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# ChangerError function



## -description
<p><b>ChangerError</b> performs device-specific error handling. </p>


## -syntax

````
VOID ChangerError(
   PDEVICE_OBJECT      DeviceObject,
   PSCSI_REQUEST_BLOCK Srb,
   NTSTATUS            *Status,
   BOOLEAN             *Retry
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> 

<dd>
<p>Pointer to the device object that represents the changer. </p>
</dd>

### -param <i>Srb</i> 

<dd>
<p>Pointer to the SCSI request block for the operation that failed.</p>
</dd>

### -param <i>Status</i> 

<dd>
<p>Specifies the address of the STATUS_<i>XXX</i> code set by the system. The changer miniclass driver can change the status or leave it as is.</p>
</dd>

### -param <i>Retry</i> 

<dd>
<p>Pointer to a flag that indicates whether to retry the request. The changer miniclass driver can set this flag or leave it as is.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks
<p>This routine is required.</p>

<p>If an SRB fails with a SCSI status of CHECK CONDITION, the SCSI class driver calls the changer class driver's <b>ChangerClassError</b> routine. <b>ChangerClassError</b> performs device-independent error handling and calls the changer miniclass driver's <b>ChangerError</b> routine.</p>

<p><b>ChangerError</b> first checks <i>Srb</i><b>-&gt;SrbStatus</b> with SRB_STATUS_AUTOSENSE_VALID to make sure the sense data buffer is valid. If so, it checks the sense data in <i>Srb</i><b>-&gt;SenseInfoBuffer</b> to determine whether to update <i>*Status</i> with a more accurate STATUS_<i>XXX</i> code and/or set the <i>Retry</i> flag before returning to the changer class driver. The changer class driver's retry count determines whether the SRB is actually retried. </p>

<p>This routine is required.</p>

<p>If an SRB fails with a SCSI status of CHECK CONDITION, the SCSI class driver calls the changer class driver's <b>ChangerClassError</b> routine. <b>ChangerClassError</b> performs device-independent error handling and calls the changer miniclass driver's <b>ChangerError</b> routine.</p>

<p><b>ChangerError</b> first checks <i>Srb</i><b>-&gt;SrbStatus</b> with SRB_STATUS_AUTOSENSE_VALID to make sure the sense data buffer is valid. If so, it checks the sense data in <i>Srb</i><b>-&gt;SenseInfoBuffer</b> to determine whether to update <i>*Status</i> with a more accurate STATUS_<i>XXX</i> code and/or set the <i>Retry</i> flag before returning to the changer class driver. The changer class driver's retry count determines whether the SRB is actually retried. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Mcd.h (include Mcd.h or Ntddchgr.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>
---
UID: NF.srb.ScsiPortGetSrb
title: ScsiPortGetSrb
author: windows-driver-content
description: The ScsiPortGetSrb routine returns a pointer to an active SCSI request for a particular logical unit.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
old-location: storage\scsiportgetsrb.htm
old-project: storage
ms.assetid: c8f0e47c-4d06-445f-a6dd-9bd80fc490bc
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: ScsiPortGetSrb
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: srb.h
req.include-header: Miniport.h, Scsi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ScsiPortGetSrb
req.alt-loc: Scsiport.lib,Scsiport.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Scsiport.lib
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# ScsiPortGetSrb function



## -description
<p>The <b>ScsiPortGetSrb</b> routine returns a pointer to an active SCSI request for a particular logical unit.</p>


## -syntax

````
PSCSI_REQUEST_BLOCK ScsiPortGetSrb(
  _In_ PVOID DeviceExtension,
  _In_ UCHAR PathId,
  _In_ UCHAR TargetId,
  _In_ UCHAR Lun,
  _In_ LONG  QueueTag
);
````


## -parameters
<dl>

### -param DeviceExtension [in]

<dd>
<p>Pointer to the miniport driver's per-HBA storage area.</p>
</dd>

### -param PathId [in]

<dd>
<p>Identifies the SCSI bus.</p>
</dd>

### -param TargetId [in]

<dd>
<p>Identifies the target controller or device on the bus.</p>
</dd>

### -param Lun [in]

<dd>
<p>Identifies the logical unit number of the target device.</p>
</dd>

### -param QueueTag [in]

<dd>
<p>Specifies the queue tag if the miniport driver handles tagged requests; SP_UNTAGGED indicates that the request is not tagged.</p>
</dd>
</dl>

## -returns
<p><b>ScsiPortGetSrb</b> returns a pointer to a request for the specified logical unit. If there is no outstanding request for the given peripheral or if the <i>QueueTag</i> value is invalid, it returns <b>NULL</b>.</p>

## -remarks


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
<dt>Srb.h (include Miniport.h or Scsi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Scsiport.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\srb\ns-srb--scsi-request-block.md">SCSI_REQUEST_BLOCK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20ScsiPortGetSrb routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NS.wdfio._WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY_SETTINGS
title: WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY_SETTINGS
author: windows-driver-content
description: The WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY_SETTINGS structure contains information about specific actions that the framework can take when it receives an I/O request for your driver, if a low-memory situation exists.
old-location: wdf\wdf_io_forward_progress_reserved_policy_settings.htm
old-project: wdf
ms.assetid: 28ffe82f-79b6-4a00-b4fa-36df5df303a6
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY_SETTINGS, WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY_SETTINGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfio.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.9
req.umdf-ver: 
req.alt-api: WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY_SETTINGS
req.alt-loc: wdfio.h
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
req.product: Windows 10 or later.
---

# WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY_SETTINGS structure



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY_SETTINGS</b> structure contains information about specific actions that the framework can take when it receives an I/O request for your driver, if a low-memory situation exists.</p>


## -syntax

````
typedef struct _WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY_SETTINGS {
  union {
    struct {
      PFN_WDF_IO_WDM_IRP_FOR_FORWARD_PROGRESS EvtIoWdmIrpForForwardProgress;
    } ExaminePolicy;
  } Policy;
} WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY_SETTINGS;
````


## -struct-fields
<dl>

### -field <b>Policy</b>

<dd>
<dl>

### -field <b>ExaminePolicy</b>

<dd>
<dl>

### -field <b>EvtIoWdmIrpForForwardProgress</b>

<dd>
<p>A pointer to the driver's queue-specific <a href="..\wdfio\nc-wdfio-evt-wdf-io-wdm-irp-for-forward-progress.md">EvtIoWdmIrpForForwardProgress</a> callback function.</p>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The <b>WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY_SETTINGS</b> structure is used as a member type in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552364">WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.9</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfio.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>
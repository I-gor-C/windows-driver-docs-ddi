---
UID: NF.irb.AtaPortControllerSyncRoutine
title: AtaPortControllerSyncRoutine
author: windows-driver-content
description: The AtaPortControllerSyncRoutine routine provides synchronized access to data structures that are shared across all channels on a controller.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\ataportcontrollersyncroutine.htm
ms.assetid: 6b39e89e-21cc-404f-b9fc-6cad0b5c8d22
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: Storage
req.header: irb.h
req.include-header: Ata.h, Irb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AtaPortControllerSyncRoutine
req.alt-loc: irb.h
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
ms.keywords: AtaPortControllerSyncRoutine
req.iface: 
---

# AtaPortControllerSyncRoutine function



## -description
<p>The <b>AtaPortControllerSyncRoutine</b> routine provides synchronized access to data structures that are shared across all channels on a controller.</p>


## -syntax

````
BOOLEAN __inline AtaPortControllerSyncRoutine(
  _In_ PVOID      ChannelExtension,
  _In_ IDE_HW_DPC ControllerSyncRoutine
);
````


## -parameters
<dl>

### -param <i>ChannelExtension</i> [in]

<dd>
<p>A pointer to the channel extension. </p>
</dd>

### -param <i>ControllerSyncRoutine</i> [in]

<dd>
<p>A pointer to the routine to call. </p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p>The miniport driver uses this routine to synchronize access to data structures that are shared across channels on a controller. The miniport driver, however, should use this routine very sparingly.</p>

<p>The <i>ControllerSyncRoutine</i> function pointer is declared in <i>Irb.h</i> as follows:</p>

<p>The miniport driver uses this routine to synchronize access to data structures that are shared across channels on a controller. The miniport driver, however, should use this routine very sparingly.</p>

<p>The <i>ControllerSyncRoutine</i> function pointer is declared in <i>Irb.h</i> as follows:</p>

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
<dt>Irb.h (include Ata.h or Irb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550223">AtaPortRequestSynchronizedRoutine</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20AtaPortControllerSyncRoutine routine%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

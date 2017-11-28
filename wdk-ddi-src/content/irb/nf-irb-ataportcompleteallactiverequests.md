---
UID: NF.irb.AtaPortCompleteAllActiveRequests
title: AtaPortCompleteAllActiveRequests
author: windows-driver-content
description: The AtaPortCompleteAllActiveRequests routine completes all active IRBs for the indicated device.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\ataportcompleteallactiverequests.htm
old-project: storage
ms.assetid: e17b1a76-ab1e-4263-9e4a-42c6f2066de1
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: AtaPortCompleteAllActiveRequests
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: irb.h
req.include-header: Ata.h, Irb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AtaPortCompleteAllActiveRequests
req.alt-loc: ataport.lib,ataport.dll,pciidex.lib,pciidex.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ataport.lib; 
Pciidex.lib
req.dll: 
req.irql: 
req.iface: 
---

# AtaPortCompleteAllActiveRequests function



## -description
<p>The <b>AtaPortCompleteAllActiveRequests</b> routine completes all active IRBs for the indicated device.</p>


## -syntax

````
VOID AtaPortCompleteAllActiveRequests(
  _In_ PVOID ChannelExtension,
  _In_ UCHAR Target,
  _In_ UCHAR Lun,
  _In_ UCHAR IrbStatus
);
````


## -parameters
<dl>

### -param <i>ChannelExtension</i> [in]

<dd>
<p>A pointer to the channel extension.</p>
</dd>

### -param <i>Target</i> [in]

<dd>
<p>Specifies the target identifier of the device.</p>
</dd>

### -param <i>Lun</i> [in]

<dd>
<p>Specifies the logical unit number of the device.</p>
</dd>

### -param <i>IrbStatus</i> [in]

<dd>
<p>Specifies the status with which the requests will be completed.</p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p>The <b>AtaPortCompleteAllActiveRequests</b> routine completes all active IRBs on the device as indicated by the <i>Target </i>and <i>Lun</i> parameters. Miniport drivers use this routine to complete all active IRPs if there is a reset. Miniport drivers can complete IRBs on all devices concurrently by assigning a value of IDE_UNTAGGED to the <i>Target </i>and <i>Lun </i>parameters, instead of specifying a specific device.</p>

<p>The miniport driver must not call this routine from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558992">IdeHwInterrupt</a> routine.</p>

<p>The <b>AtaPortCompleteAllActiveRequests</b> routine completes all active IRBs on the device as indicated by the <i>Target </i>and <i>Lun</i> parameters. Miniport drivers use this routine to complete all active IRPs if there is a reset. Miniport drivers can complete IRBs on all devices concurrently by assigning a value of IDE_UNTAGGED to the <i>Target </i>and <i>Lun </i>parameters, instead of specifying a specific device.</p>

<p>The miniport driver must not call this routine from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff558992">IdeHwInterrupt</a> routine.</p>

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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ataport.lib; </dt>
<dt>Pciidex.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558992">IdeHwInterrupt</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20AtaPortCompleteAllActiveRequests routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

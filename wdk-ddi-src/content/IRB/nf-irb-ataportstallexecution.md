---
UID: NF.irb.AtaPortStallExecution
title: AtaPortStallExecution
author: windows-driver-content
description: The AtaPortStallExecution stalls in the miniport driver.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\ataportstallexecution.htm
ms.assetid: 5dae484f-fb79-4291-bae5-dba0be7f9b97
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
req.alt-api: AtaPortStallExecution
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
ms.keywords: AtaPortStallExecution
req.iface: 
---

# AtaPortStallExecution function



## -description
<p>The <b>AtaPortStallExecution</b> stalls in the miniport driver.</p>


## -syntax

````
VOID AtaPortStallExecution(
  _In_ ULONG Delay
);
````


## -parameters
<dl>

### -param <i>Delay</i> [in]

<dd>
<p>Specifies the delay interval, in microseconds.</p>
</dd>
</dl>

## -returns
<p>None </p>

## -remarks
<p>Miniport drivers should rarely call the <b>AtaPortStallExecution</b> routine. The total stall time in any miniport driver routine must always be less than one millisecond. Because this call ties up a processor, the processor does no useful work while it stalls in the driver.</p>

<p>Typically, a miniport driver should call <b>AtaPortStallExecution</b> only if the driver must wait for some sort of state change on the HBA that is unable to cause an interrupt, or if the driver must delay for a very short interval between accesses to the HBA.</p>

<p>Miniport drivers should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550227">AtaPortRequestTimer</a> routine for delays longer than 1 millisecond.</p>

<p>Miniport drivers should rarely call the <b>AtaPortStallExecution</b> routine. The total stall time in any miniport driver routine must always be less than one millisecond. Because this call ties up a processor, the processor does no useful work while it stalls in the driver.</p>

<p>Typically, a miniport driver should call <b>AtaPortStallExecution</b> only if the driver must wait for some sort of state change on the HBA that is unable to cause an interrupt, or if the driver must delay for a very short interval between accesses to the HBA.</p>

<p>Miniport drivers should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550227">AtaPortRequestTimer</a> routine for delays longer than 1 millisecond.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550227">AtaPortRequestTimer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20AtaPortStallExecution function%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

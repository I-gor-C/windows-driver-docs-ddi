---
UID: NE.wdm.DMA_COMPLETION_STATUS
title: DMA_COMPLETION_STATUS
author: windows-driver-content
description: The DMA_COMPLETION_STATUS enumeration describes the completion status of a DMA transfer.
old-location: kernel\dma_completion_status.htm
old-project: kernel
ms.assetid: 12F6E1F5-15F9-42BE-8C47-C9A561513717
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DMA_COMPLETION_STATUS
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# DMA_COMPLETION_STATUS enumeration



## -description
<p>
<p>The <b>DMA_COMPLETION_STATUS</b> enumeration describes the completion status of a DMA transfer.</p>
</p>
<p>The <b>DMA_COMPLETION_STATUS</b> enumeration describes the completion status of a DMA transfer.</p>


## -syntax

````
typedef enum  { 
  DmaComplete,
  DmaAborted,
  DmaError,
  DmaCancelled
} DMA_COMPLETION_STATUS;
````


## -enum-fields
<dl>

### -field <a id="DmaComplete"></a><a id="dmacomplete"></a><a id="DMACOMPLETE"></a><b>DmaComplete</b>

<dd>
<p>The DMA transfer completed successfully.</p>
</dd>

### -field <a id="DmaAborted"></a><a id="dmaaborted"></a><a id="DMAABORTED"></a><b>DmaAborted</b>

<dd>
<p>Not used.</p>
</dd>

### -field <a id="DmaError"></a><a id="dmaerror"></a><a id="DMAERROR"></a><b>DmaError</b>

<dd>
<p>The DMA transfer did not complete successfully because an error occurred.</p>
</dd>

### -field <a id="DmaCancelled"></a><a id="dmacancelled"></a><a id="DMACANCELLED"></a><b>DmaCancelled</b>

<dd>
<p>The DMA transfer did not complete successfully because the client canceled the transfer.</p>
</dd>
</dl>

## -remarks
<p>The <i>Status</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450991">DmaCompletionRoutine</a> routine is a <b>DMA_COMPLETION_STATUS</b>  enumeration value.</p>

<p>The <i>Status</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450991">DmaCompletionRoutine</a> routine is a <b>DMA_COMPLETION_STATUS</b>  enumeration value.</p>

<p>The <i>Status</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450991">DmaCompletionRoutine</a> routine is a <b>DMA_COMPLETION_STATUS</b>  enumeration value.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with  Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450991">DmaCompletionRoutine</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20DMA_COMPLETION_STATUS enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

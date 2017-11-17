---
UID: NE.wdfdmaenabler._WDF_DMA_DIRECTION
title: WDF_DMA_DIRECTION
author: windows-driver-content
description: The WDF_DMA_DIRECTION enumeration defines the direction of a DMA transfer.
old-location: wdf\wdf_dma_direction.htm
ms.assetid: 813414fa-17b6-4b69-a3dd-f3a2e5190305
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdmaenabler.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_DMA_DIRECTION
req.alt-loc: wdfdmaenabler.h
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
ms.keywords: WDF_REMOVE_LOCK_OPTIONS, WDF_REMOVE_LOCK_OPTIONS, *PWDF_REMOVE_LOCK_OPTIONS
req.iface: 
req.product: Windows 10 or later.
---

# WDF_DMA_DIRECTION enumeration



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_DMA_DIRECTION</b> enumeration defines the direction of a DMA transfer.</p>


## -syntax

````
typedef enum _WDF_DMA_DIRECTION { 
  WdfDmaDirectionReadFromDevice  = FALSE,
  WdfDmaDirectionWriteToDevice   = TRUE
} WDF_DMA_DIRECTION;
````


## -enum-fields
<dl>

### -field <a id="WdfDmaDirectionReadFromDevice"></a><a id="wdfdmadirectionreadfromdevice"></a><a id="WDFDMADIRECTIONREADFROMDEVICE"></a><b>WdfDmaDirectionReadFromDevice</b>

<dd>
<p>The DMA transfer direction is from the device (read).</p>
</dd>

### -field <a id="WdfDmaDirectionWriteToDevice"></a><a id="wdfdmadirectionwritetodevice"></a><a id="WDFDMADIRECTIONWRITETODEVICE"></a><b>WdfDmaDirectionWriteToDevice</b>

<dd>
<p>The DMA transfer direction is to the device (write).</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_DMA_DIRECTION</b> enumeration is used as input to the <a href="https://msdn.microsoft.com/c01b94b2-aabf-47dd-952a-06e481579614">EvtProgramDma</a> callback function and the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547099">WdfDmaTransactionInitialize</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff547107">WdfDmaTransactionInitializeUsingRequest</a> methods.</p>

<p>The <b>WDF_DMA_DIRECTION</b> enumeration is used as input to the <a href="https://msdn.microsoft.com/c01b94b2-aabf-47dd-952a-06e481579614">EvtProgramDma</a> callback function and the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547099">WdfDmaTransactionInitialize</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff547107">WdfDmaTransactionInitializeUsingRequest</a> methods.</p>

<p>The <b>WDF_DMA_DIRECTION</b> enumeration is used as input to the <a href="https://msdn.microsoft.com/c01b94b2-aabf-47dd-952a-06e481579614">EvtProgramDma</a> callback function and the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547099">WdfDmaTransactionInitialize</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff547107">WdfDmaTransactionInitializeUsingRequest</a> methods.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdmaenabler.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/c01b94b2-aabf-47dd-952a-06e481579614">EvtProgramDma</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547099">WdfDmaTransactionInitialize</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547107">WdfDmaTransactionInitializeUsingRequest</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_DMA_DIRECTION enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

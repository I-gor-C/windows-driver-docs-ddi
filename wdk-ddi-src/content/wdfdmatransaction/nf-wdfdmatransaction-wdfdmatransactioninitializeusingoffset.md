---
UID: NF.wdfdmatransaction.WdfDmaTransactionInitializeUsingOffset
title: WdfDmaTransactionInitializeUsingOffset function
author: windows-driver-content
description: The WdfDmaTransactionInitializeUsingOffset method initializes a specified DMA transaction by using a byte offset into an MDL chain.
old-location: wdf\wdfdmatransactioninitializeusingoffset.htm
old-project: wdf
ms.assetid: 896343A8-0C72-47D4-8465-A029EDCD66A0
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfDmaTransactionInitializeUsingOffset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdmatransaction.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 
req.alt-api: WdfDmaTransactionInitializeUsingOffset
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfDmaTransactionInitializeUsingOffset function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The 
   <b>WdfDmaTransactionInitializeUsingOffset</b> method initializes a specified DMA transaction by using a byte offset into an MDL chain.



## -syntax

````
NTSTATUS WdfDmaTransactionInitializeUsingOffset(
  _In_ WDFDMATRANSACTION   DmaTransaction,
  _In_ PFN_WDF_PROGRAM_DMA EvtProgramDmaFunction,
  _In_ WDF_DMA_DIRECTION   DmaDirection,
  _In_ PMDL                Mdl,
  _In_ size_t              Offset,
  _In_ size_t              Length
);
````


## -parameters

### -param DmaTransaction [in]

A handle to a DMA transaction object that the driver obtained from a previous call to <a href="wdf.wdfdmatransactioncreate">WdfDmaTransactionCreate</a>.


### -param EvtProgramDmaFunction [in]

A pointer to the driver's <a href="wdf.evtprogramdma">EvtProgramDma</a> event callback function. 


### -param DmaDirection [in]

A <a href="wdf.wdf_dma_direction">WDF_DMA_DIRECTION</a>-typed value.


### -param Mdl [in]

A pointer to a memory descriptor list (MDL) that describes the buffer that will be used for the DMA transaction. See more information in <b>Remarks</b>.


### -param Offset [in]

The byte offset into the MDL chain for the current transaction.


### -param Length [in]

The number of bytes to be transferred. This value must be greater than zero.


## -returns
<b>WdfDmaTransactionInitializeUsingOffset</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, the method might return one of the values described in the Return values section of <a href="wdf.wdfdmatransactioninitialize">WdfDmaTransactionInitialize</a>.

This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
<b>WdfDmaTransactionInitializeUsingOffset</b> is equivalent to <a href="wdf.wdfdmatransactioninitialize">WdfDmaTransactionInitialize</a> except that it takes an offset into the buffer described by the MDL chain rather than a virtual address.

The driver can specify an MDL chain in the <i>Mdl</i> parameter of this method. An MDL chain is a sequence of MDL structures that the driver chained together using the <b>Next</b> member of the MDL structure.


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
Minimum KMDF version

</th>
<td width="70%">
1.11

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfdmatransaction.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
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
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfdmatransactioninitialize">WdfDmaTransactionInitialize</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDmaTransactionInitializeUsingOffset method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


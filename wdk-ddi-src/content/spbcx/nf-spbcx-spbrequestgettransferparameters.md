---
UID: NF.spbcx.SpbRequestGetTransferParameters
title: SpbRequestGetTransferParameters
author: windows-driver-content
description: The SpbRequestGetTransferParameters method retrieves the transfer parameters for an individual transfer in an I/O transfer sequence.
old-location: spb\spbrequestgettransferparameters.htm
old-project: SPB
ms.assetid: 33B0C9EF-B40A-4BE7-A5AB-81FFF4698F3F
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: SpbRequestGetTransferParameters
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: spbcx.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SpbRequestGetTransferParameters
req.alt-loc: spbcxstubs.lib,spbcxstubs.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Spbcxstubs.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# SpbRequestGetTransferParameters function



## -description
<p>The <b>SpbRequestGetTransferParameters</b> method retrieves the transfer parameters for an individual transfer in an <a href="https://msdn.microsoft.com/7415DB28-5E93-4F47-B169-7C652969D4C7">I/O transfer sequence</a>.</p>


## -syntax

````
void SpbRequestGetTransferParameters(
  _In_      SPBREQUEST              SpbRequest,
  _In_      ULONG                   Index,
  _Out_opt_ SPB_TRANSFER_DESCRIPTOR *TransferDescriptor,
  _Out_opt_ PMDL                    *TransferBuffer
);
````


## -parameters
<dl>

### -param SpbRequest [in]

<dd>
<p>An <a href="buses.spbrequest_object_handle">SPBREQUEST</a> handle to the I/O request from which to retrieve the transfer parameters. This parameter must be a handle to an <a href="https://msdn.microsoft.com/library/windows/hardware/hh450857">IOCTL_SPB_EXECUTE_SEQUENCE</a> request.</p>
</dd>

### -param Index [in]

<dd>
<p>The index of a transfer in the I/O transfer sequence. For more information, see the following Remarks section.</p>
</dd>

### -param TransferDescriptor [out, optional]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/hh406218">SPB_TRANSFER_DESCRIPTOR</a> structure into which  the method writes the transfer parameters. The <i>TransferDescriptor</i> parameter is optional and can be specified as NULL if the caller does not require the transfer parameters. For more information, see the following Remarks section.</p>
</dd>

### -param TransferBuffer [out, optional]

<dd>
<p>A pointer to a location into which the method writes a pointer to an MDL (or an MDL chain) that describes the physical memory in the transfer buffer.  The caller must not modify the contents of this MDL. This parameter is optional and can be set to NULL if the MDL is not needed. For more information, see the following Remarks section.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>To request an I/O transfer sequence, a client (peripheral driver) of the SPB controller driver sends an <a href="https://msdn.microsoft.com/library/windows/hardware/hh450857">IOCTL_SPB_EXECUTE_SEQUENCE</a> request that contains a list of the transfers in the sequence. Your controller driver can call <b>SpbRequestGetTransferParameters</b> to obtain information about a particular transfer in the sequence.</p>

<p>The <i>Index</i> parameter is an index that identifies a particular transfer in the sequence.   If N is the number of transfers in the sequence, valid indexes range from 0 to N–1. To determine the number of transfers in the sequence, call the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450922">SpbRequestGetParameters</a> method. This method retrieves an <a href="https://msdn.microsoft.com/library/windows/hardware/hh406218">SPB_TRANSFER_DESCRIPTOR</a> structure that contains the request parameters. The <b>TransferCount</b> member of this structure specifies the number of transfers in the sequence.</p>

<p>If <i>TransferDescriptor</i> is non-NULL, the caller must call the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406219">SPB_TRANSFER_DESCRIPTOR_INIT</a> function to initialize the structure before calling  <b>SpbRequestGetTransferParameters</b>.  After the structure is initialized, it can be reused as many times as needed without being reinitialized.</p>

<p><i>TransferBuffer</i> is an optional pointer into which <b>SpbRequestGetTransferParameters</b> writes a pointer to an MDL that describes the physical page layout for the transfer buffer. The transfer buffer can be described by a single MDL or by an MDL chain. A simple buffer, which consists of a contiguous block of virtual memory, is described by a single MDL. If a transfer buffer is formatted as a scatter-gather list, each contiguous block of virtual memory in the buffer is described by an MDL in an MDL chain. For more information about MDLs, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565421">Using MDLs</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Spbcx.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Spbcxstubs.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450857">IOCTL_SPB_EXECUTE_SEQUENCE</a>
</dt>
<dt>
<a href="buses.spbrequest_object_handle">SPBREQUEST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450922">SpbRequestGetParameters</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406218">SPB_TRANSFER_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406219">SPB_TRANSFER_DESCRIPTOR_INIT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [SPB\buses]:%20SpbRequestGetTransferParameters method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

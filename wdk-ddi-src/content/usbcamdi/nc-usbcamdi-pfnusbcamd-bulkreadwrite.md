---
UID: NC.usbcamdi.PFNUSBCAMD_BulkReadWrite
title: PFNUSBCAMD_BulkReadWrite
author: windows-driver-content
description: The USBCAMD_BulkReadWrite service performs a read or write operation on the specified bulk pipe.
old-location: stream\usbcamd_bulkreadwrite.htm
old-project: stream
ms.assetid: 4888e6a7-be44-4ed9-80be-9dd7641653ef
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: USBC_FUNCTION_DESCRIPTOR, USBC_FUNCTION_DESCRIPTOR, *PUSBC_FUNCTION_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: usbcamdi.h
req.include-header: Usbcamdi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBCAMD_BulkReadWrite
req.alt-loc: usbcamdi.h
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
req.iface: 
req.product: Windows 10 or later.
---

# PFNUSBCAMD_BulkReadWrite callback



## -description
<p>The <b>USBCAMD_BulkReadWrite</b> service performs a read or write operation on the specified bulk pipe.</p>


## -prototype

````
PFNUSBCAMD_BulkReadWrite USBCAMD_BulkReadWrite;

NTSTATUS APIENTRY USBCAMD_BulkReadWrite(
  _In_ PVOID                      DeviceContext,
  _In_ USHORT                     PipeIndex,
  _In_ PVOID                      Buffer,
  _In_ ULONG                      BufferLength,
  _In_ PCOMMAND_COMPLETE_FUNCTION CommandComplete,
  _In_ PVOID                      CommandContext
)
{ ... }
````


## -parameters
<dl>

### -param <i>DeviceContext</i> [in]

<dd>
<p>Pointer to the camera minidriver's device context.</p>
</dd>

### -param <i>PipeIndex</i> [in]

<dd>
<p>Specifies the index of the bulk pipe.</p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>Pointer to the read or write buffer. If this parameter is set to <b>NULL</b> for a read request, USBCAMD pulls a data SRB from the SRB read queue of the stream associated with this pipe. Write requests with a <b>NULL</b> buffer pointer are only permitted on the still pin if an SRB_WRITE_DATA request has been submitted to the still pin.</p>
</dd>

### -param <i>BufferLength</i> [in]

<dd>
<p>Specifies the length of the read/write buffer in bytes.</p>
</dd>

### -param <i>CommandComplete</i> [in]

<dd>
<p>Pointer to a camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557713">CommandCompleteFunction</a>, which is called when the bulk read or write is completed. This value can be <b>NULL</b>.</p>
</dd>

### -param <i>CommandContext</i> [in]

<dd>
<p>Pointer to a block of memory, that is passed as an argument to the camera minidriver defined <a href="https://msdn.microsoft.com/library/windows/hardware/ff557713">CommandCompleteFunction</a>.</p>
</dd>
</dl>

## -returns
<p><b>USBCAMD_BulkReadWrite</b> returns STATUS_SUCCESS if the call was successful. Other possible error codes include:</p><dl>
<dt><b>STATUS_FILE_CLOSED</b></dt>
</dl><p>The device has been removed.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>USBCAMD may return STATUS_INVALID_PARAMETER for a number of reasons, including:</p>

<p>The value passed in the <i>PipeIndex</i> argument is invalid.</p>

<p>The type of the pipe specified by the <i>PipeIndex</i> argument represents an invalid type of pipe.</p>

<p>A bulk read/write request already exists.</p>

<p>The <i>Buffer</i> argument is <b>NULL</b>.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>There are insufficient resources to schedule a transfer.</p>

<p> </p>

## -remarks
<p>USBCAMD can accept one read and one write request at a time.</p>

<p><b>USBCAMD_BulkReadWrite</b> is not available in USBCAMD version 1.0.</p>

<p>USBCAMD can accept one read and one write request at a time.</p>

<p><b>USBCAMD_BulkReadWrite</b> is not available in USBCAMD version 1.0.</p>

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
<dt>Usbcamdi.h (include Usbcamdi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568605">USBCAMD_INTERFACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557713">CommandCompleteFunction</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20USBCAMD_BulkReadWrite routine%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NS.spb.SPB_TRANSFER_BUFFER
title: SPB_TRANSFER_BUFFER
author: windows-driver-content
description: The SPB_TRANSFER_BUFFER structure describes the data buffer for an individual transfer in an I/O transfer sequence.
old-location: spb\spb_transfer_buffer.htm
old-project: SPB
ms.assetid: E9C5B866-1EB0-4043-B22F-DF2F4CFAE64C
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SPB_TRANSFER_BUFFER,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: spb.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SPB_TRANSFER_BUFFER
req.alt-loc: Spb.h
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

# SPB_TRANSFER_BUFFER structure



## -description
<p>The <b>SPB_TRANSFER_BUFFER</b> structure describes the data buffer for an individual transfer in an <a href="https://msdn.microsoft.com/7415DB28-5E93-4F47-B169-7C652969D4C7">I/O transfer sequence</a>.</p>


## -syntax

````
typedef struct _SPB_TRANSFER_BUFFER {
  SPB_TRANSFER_BUFFER_FORMAT Format;
  union {
    SPB_TRANSFER_BUFFER_LIST_ENTRY Simple;
    struct {
      PSPB_TRANSFER_BUFFER_LIST_ENTRY List;
      ULONG                           ListCe;
    } BufferList;
    PMDL                           Mdl;
  };
} SPB_TRANSFER_BUFFER, *PSPB_TRANSFER_BUFFER;
````


## -struct-fields
<dl>

### -field <b>Format</b>

<dd>
<p>The buffer format.  This member is set to one of the following <a href="https://msdn.microsoft.com/library/windows/hardware/hh406216">SPB_TRANSFER_BUFFER_FORMAT</a> enumeration values:</p>
<ul>
<li><b>SpbTransferBufferFormatSimple</b></li>
<li><b>SpbTransferBufferFormatList</b></li>
<li><b>SpbTransferBufferFormatSimpleNonPaged</b></li>
<li><b>SpbTransferBufferFormatMdl</b></li>
</ul>
<p><b>SpbTransferBufferFormatMdl</b> is a valid value only for I/O transfer sequences that are requested by clients of the SPB controller driver that are kernel-mode components.</p>
</dd>

### -field <b>Simple</b>

<dd>
<p>A SPB_TRANSFER_BUFFER_LIST_ENTRY  structure that specifies the base address and the length of a simple transfer buffer. Use this member of the union if <b>Format</b> is <b>SpbTransferBufferFormatSimple</b> or <b>SpbTransferBufferFormatSimpleNonPaged</b>. The <b>SpbTransferBufferFormatSimpleNonPaged</b> format is used only by kernel-mode clients.</p>
</dd>

### -field <b>BufferList</b>

<dd>
<p>A scatter-gather list that consists of an array of buffer descriptors. Use this member of the union if <b>Format</b> is <b>SpbTransferBufferFormatList</b>.</p>
<dl>

### -field <b>List</b>

<dd>
<p>A pointer to an array of <b>SPB_TRANSFER_BUFFER_LIST_ENTRY</b> structures that describe the buffers in the scatter-gather list.</p>
</dd>

### -field <b>ListCe</b>

<dd>
<p>The number of elements in the <b>List</b> array.</p>
</dd>
</dl>
</dd>

### -field <b>Mdl</b>

<dd>
<p>A pointer to an MDL that describes the buffer. This member is used only by kernel-mode clients. Use this member of the union if <b>Format</b> is <b>SpbTransferBufferFormatMdl</b>. For more information, see Remarks.</p>
</dd>
</dl>

## -remarks
<p>This structure is used by an <a href="https://msdn.microsoft.com/library/windows/hardware/hh406223">SPB_TRANSFER_LIST_ENTRY</a> structure to describe a transfer buffer.</p>

<p>The <b>Mdl</b> member of this structure can be used only by clients of the SPB controller driver that are kernel-mode components. User-mode clients must not use this member. For more information about MDLs, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565421">Using MDLs</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Spb.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406216">SPB_TRANSFER_BUFFER_FORMAT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406217">SPB_TRANSFER_BUFFER_LIST_ENTRY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406223">SPB_TRANSFER_LIST_ENTRY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [SPB\buses]:%20SPB_TRANSFER_BUFFER structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NS.wdfcommonbuffer._WDF_COMMON_BUFFER_CONFIG
title: WDF_COMMON_BUFFER_CONFIG
author: windows-driver-content
description: The WDF_COMMON_BUFFER_CONFIG structure contains configuration information for a common buffer.
old-location: wdf\wdf_common_buffer_config.htm
old-project: wdf
ms.assetid: 19e98448-6951-4eb4-bca1-8119cd6f7713
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_COMMON_BUFFER_CONFIG, WDF_COMMON_BUFFER_CONFIG, *PWDF_COMMON_BUFFER_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfcommonbuffer.h
req.include-header: WdfCommonBuffer.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_COMMON_BUFFER_CONFIG
req.alt-loc: wdfcommonbuffer.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WDF_COMMON_BUFFER_CONFIG structure



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_COMMON_BUFFER_CONFIG</b> structure contains configuration information for a common buffer.</p>


## -syntax

````
typedef struct _WDF_COMMON_BUFFER_CONFIG {
  ULONG Size;
  ULONG AlignmentRequirement;
} WDF_COMMON_BUFFER_CONFIG, *PWDF_COMMON_BUFFER_CONFIG;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>AlignmentRequirement</b>

<dd>
<p>The alignment requirement for a common buffer. This value must be one less than the alignment boundary. For example, you can specify 15 for a 16-byte alignment boundary and 31 for a 32-byte alignment boundary. You can also use one of the FILE_<i>Xxxx</i>_ALIGNMENT constants that are defined in <i>Wdm.h</i>.   </p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_COMMON_BUFFER_CONFIG</b> structure is used as input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545805">WdfCommonBufferCreateWithConfig</a> method.</p>

<p>If your driver specifies an alignment requirement that is greater that the computer's page size (PAGE_SIZE), the logical addresses that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545814">WdfCommonBufferGetAlignedLogicalAddress</a> method returns are always aligned to the specified alignment requirement, but the virtual addresses that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545820">WdfCommonBufferGetAlignedVirtualAddress</a> method returns might not be aligned to the alignment requirement.</p>

<p>If your driver specifies an alignment requirement that is less than the computer's page size, all logical and virtual addresses are aligned to the specified alignment requirement.</p>

<p>For more information about specifying alignment requirements, see <a href="wdf.enabling_dma_transactions">Enabling DMA Transactions</a> and <a href="wdf.using_common_buffers">Using Common Buffers</a>.</p>

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
<dt>Wdfcommonbuffer.h (include WdfCommonBuffer.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545805">WdfCommonBufferCreateWithConfig</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545814">WdfCommonBufferGetAlignedLogicalAddress</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545820">WdfCommonBufferGetAlignedVirtualAddress</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_COMMON_BUFFER_CONFIG structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

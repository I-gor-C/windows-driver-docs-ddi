---
UID: NF.wudfddi.IWDFMemory.CopyFromMemory
title: IWDFMemory::CopyFromMemory
author: windows-driver-content
description: The CopyFromMemory method safely copies data from the specified source buffer and prevents overruns that the copy operation might otherwise cause.
old-location: wdf\iwdfmemory_copyfrommemory.htm
old-project: wdf
ms.assetid: 29b77215-9c7e-47f2-8c94-0bcd733f54a2
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFMemory, CopyFromMemory, IWDFMemory::CopyFromMemory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFMemory.CopyFromMemory
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: <= DISPATCH_LEVEL
req.iface: IWDFMemory
req.product: Windows 10 or later.
---

# IWDFMemory::CopyFromMemory method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>CopyFromMemory</b> method safely copies data from the specified source buffer and prevents overruns that the copy operation might otherwise cause.</p>


## -syntax

````
HRESULT CopyFromMemory(
  [in]           IWDFMemory        *pSource,
  [in, optional] PWDFMEMORY_OFFSET pSourceOffset
);
````


## -parameters
<dl>

### -param <i>pSource</i> [in]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559249">IWDFMemory</a> interface for the memory object that is the source of the copy operation.</p>
</dd>

### -param <i>pSourceOffset</i> [in, optional]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561398">WDFMEMORY_OFFSET</a> structure that describes the information that is copied from a memory block. This parameter is optional. The driver can pass <b>NULL</b> if the entire source buffer is copied. </p>
<p>The <b>BufferOffset</b> member of the WDFMEMORY_OFFSET structure, if not <b>NULL</b>, indicates the offset into the source buffer to start the copy operation from. </p>
<p>The <b>BufferLength</b> member should be set to 0; the framework ignores this member because the amount of data that is copied depends on the length and offset combination of the current destination buffer. </p>
</dd>
</dl>

## -returns
<p><b>CopyFromMemory</b> returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

## -remarks


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
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.5</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559249">IWDFMemory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561398">WDFMEMORY_OFFSET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFMemory::CopyFromMemory method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

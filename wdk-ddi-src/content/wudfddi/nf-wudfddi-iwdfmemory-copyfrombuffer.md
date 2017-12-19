---
UID: NF.wudfddi.IWDFMemory.CopyFromBuffer
title: IWDFMemory::CopyFromBuffer method
author: windows-driver-content
description: The CopyFromBuffer method safely copies data from the specified source buffer to a memory object.
old-location: wdf\iwdfmemory_copyfrombuffer.htm
old-project: wdf
ms.assetid: d8e56186-f801-4684-8919-236d2429310f
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IWDFMemory, IWDFMemory::CopyFromBuffer, CopyFromBuffer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFMemory.CopyFromBuffer
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
req.irql: 
req.product: Windows 10 or later.
---

# IWDFMemory::CopyFromBuffer method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>CopyFromBuffer</b> method safely copies data from the specified source buffer to a memory object.



## -syntax

````
HRESULT CopyFromBuffer(
  [in] ULONG_PTR DestOffset,
  [in] void      *pSourceBuffer,
  [in] SIZE_T    NumOfBytesToCopyFrom
);
````


## -parameters

### -param DestOffset [in]

The offset, in bytes, into the memory object to start to copy data to.


### -param pSourceBuffer [in]

A pointer to the source buffer that data is copied from.


### -param NumOfBytesToCopyFrom [in]

The number of bytes to copy from the buffer that <i>pSourceBuffer</i> points to.


## -returns
<b>CopyFromBuffer</b> returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes that are defined in Winerror.h.

For a code example of how to use the <b>CopyFromBuffer</b> method, see <a href="wdf.iwdfioqueue_retrievenextrequest">IWDFIoQueue::RetrieveNextRequest</a>.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
End of support

</th>
<td width="70%">
Unavailable in UMDF 2.0 and later.

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
1.5

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

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
<a href="..\wudfddi\nn-wudfddi-iwdfmemory.md">IWDFMemory</a>
</dt>
<dt>
<a href="wdf.iwdfioqueue_retrievenextrequest">IWDFIoQueue::RetrieveNextRequest</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFMemory::CopyFromBuffer method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


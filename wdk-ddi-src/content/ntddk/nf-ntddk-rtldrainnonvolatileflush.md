---
UID: NF.ntddk.RtlDrainNonVolatileFlush
title: RtlDrainNonVolatileFlush function
author: windows-driver-content
description: The routine RtlDrainNonVolatileFlush waits for the flushes initiated by RtlFlushNonVolatileMemory to finish.
old-location: ifsk\rtldrainnonvolatileflush.htm
old-project: ifsk
ms.assetid: EA1C2DF3-591C-407A-ABBF-DE615466A498
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RtlDrainNonVolatileFlush
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Winnt.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1703
req.target-min-winversvr: None supported
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlDrainNonVolatileFlush
req.alt-loc: ntddk.h
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
---

# RtlDrainNonVolatileFlush function



## -description
The routine <b>RtlDrainNonVolatileFlush</b> waits for the flushes initiated by <a href="ifsk.rtlflushnonvolatilememory">RtlFlushNonVolatileMemory</a>
    to finish.



## -syntax

````
NTSTATUS RtlDrainNonVolatileFlush(
  _In_ PVOID NvToken
);
````


## -parameters

### -param NvToken [in]

 A pointer to an opaque structure that has
        information about various properties of the non-volatile memory region which <a href="ifsk.rtlgetnonvolatiletoken">RtlGetNonVolatileToken</a> had returned.


## -returns
The routine <b>RtlDrainNonVolatileFlush</b> returns one of the following:
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><b>NvToken</b> is an invalid pointer or token.
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The request was successful.

 


## -remarks
 This routine <b>RtlDrainNonVolatileFlush</b> can also add more context to <b>NvToken</b> to help verifiers. This routine is currently not supported for Windows Server until the next major release of Windows Server.


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10, version 1703

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
None supported

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Winnt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.RtlFlushNonVolatileMemory">
RtlFlushNonVolatileMemory</a>
</dt>
<dt>
<a href="ifsk.RtlFlushNonVolatileMemoryRanges">RtlFlushNonVolatileMemoryRanges</a>
</dt>
<dt>
<a href="ifsk.RtlFreeNonVolatileToken">RtlFreeNonVolatileToken</a>
</dt>
<dt>
<a href="ifsk.RtlGetNonVolatileToken">RtlGetNonVolatileToken</a>
</dt>
<dt>
<a href="ifsk.RtlWriteNonVolatileMemory">RtlWriteNonVolatileMemory</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlDrainNonVolatileFlush routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


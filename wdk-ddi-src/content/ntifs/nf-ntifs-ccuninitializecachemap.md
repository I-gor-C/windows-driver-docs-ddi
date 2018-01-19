---
UID : NF:ntifs.CcUninitializeCacheMap
title : CcUninitializeCacheMap function
author : windows-driver-content
description : The CcUninitializeCacheMap routine stops the caching of a cached file.
old-location : ifsk\ccuninitializecachemap.htm
old-project : ifsk
ms.assetid : 00e5abd6-c2d7-4408-aaf4-27a67dd3ee51
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : CcUninitializeCacheMap
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ntifs.h
req.include-header : Ntifs.h
req.target-type : Universal
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : CcUninitializeCacheMap
req.alt-loc : NtosKrnl.exe
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.lib
req.dll : NtosKrnl.exe
req.irql : 
req.typenames : TOKEN_TYPE
---


# CcUninitializeCacheMap function
The <b>CcUninitializeCacheMap</b> routine stops the caching of a cached file.

## Syntax

````
BOOLEAN CcUninitializeCacheMap(
  _In_     PFILE_OBJECT              FileObject,
  _In_opt_ PLARGE_INTEGER            TruncateSize,
  _In_opt_ PCACHE_UNINITIALIZE_EVENT UninitializeCompleteEvent
);
````

## Parameters

`FileObject`

Pointer to a file object for the cached file.

`TruncateSize`

If specified, the file was truncated to the specified size, and the cache should be purged accordingly.

`UninitializeEvent`




## Return Value

<b>CcUninitializeCacheMap</b> returns <b>TRUE</b> if caching was stopped successfully, <b>FALSE</b> otherwise.

## Remarks

All file systems that support file caching must call <b>CcUninitializeCacheMap</b> when closing a file, whether the file is cached or not. Even if the file was created with caching disabled, the file system still must call <b>CcUninitializeCacheMap</b>.

To cache a file, use <a href="..\ntifs\nf-ntifs-ccinitializecachemap.md">CcInitializeCacheMap</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h (include Ntifs.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\ntifs\nf-ntifs-ccinitializecachemap.md">CcInitializeCacheMap</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-ccpurgecachesection.md">CcPurgeCacheSection</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20CcUninitializeCacheMap routine%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
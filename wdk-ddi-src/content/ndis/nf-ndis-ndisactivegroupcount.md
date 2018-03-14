---
UID: NF:ndis.NdisActiveGroupCount
title: NdisActiveGroupCount function
author: windows-driver-content
description: The NdisActiveGroupCount function returns the number of processor groups that are currently active in the local computer system.
old-location: netvista\ndisactivegroupcount.htm
old-project: netvista
ms.assetid: f9dbeede-b4f2-4748-8a95-692f09ded787
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: NdisActiveGroupCount, NdisActiveGroupCount function [Network Drivers Starting with Windows Vista], ndis/NdisActiveGroupCount, ndis_processor_group_ref_e0e7bb9b-d6fd-4a31-9793-f21c4b36841d.xml, netvista.ndisactivegroupcount
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: Any level
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	ndis.lib
-	ndis.dll
api_name:
-	NdisActiveGroupCount
product: Windows
targetos: Windows
req.typenames: NDIS_SHARED_MEMORY_USAGE, *PNDIS_SHARED_MEMORY_USAGE
---


# NdisActiveGroupCount function
The
  <b>NdisActiveGroupCount</b> function returns the number of processor groups that are currently active in the
  local computer system.

## Syntax

````
USHORT NdisActiveGroupCount(void);
````

## Parameters

This function has no parameters.

## Return Value

<b>NdisActiveGroupCount</b> returns a USHORT value for the number of processor groups that are currently
     active and are included in the local computer system. The number of groups is a zero-based value.

## Remarks

NDIS drivers call the 
    <b>NdisActiveGroupCount</b> function to obtain the number of processor groups that are currently active
    and are included in the local computer system.

To obtain the maximum number of groups, call the 
    <a href="..\ndis\nf-ndis-ndismaxgroupcount.md">NdisMaxGroupCount</a> function.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in NDIS 6.20 and later.  |
| **Target Platform** | Universal |
| **Header** | ndis.h (include Ndis.h) |
| **Library** | Ndis.lib |
| **IRQL** | Any level |

## See Also

<a href="..\ndis\nf-ndis-ndismaxgroupcount.md">NdisMaxGroupCount</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisActiveGroupCount function%20 RELEASE:%20(2/27/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
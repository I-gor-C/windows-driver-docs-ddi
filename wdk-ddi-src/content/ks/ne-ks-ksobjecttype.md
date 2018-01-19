---
UID : NE:ks.KSOBJECTTYPE
title : KSOBJECTTYPE
author : windows-driver-content
description : The KSOBJECTTYPE enumeration lists different types of kernel streaming objects.
old-location : stream\ksobjecttype.htm
old-project : stream
ms.assetid : ab30d24f-4f14-4a84-a6e1-1a2506b4ba87
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KSOBJECTTYPE, KSOBJECTTYPE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ks.h
req.include-header : Ks.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : KSOBJECTTYPE
req.alt-loc : ks.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : KSOBJECTTYPE
---

# KSOBJECTTYPE Enumeration
The KSOBJECTTYPE enumeration lists different types of kernel streaming objects.

## Syntax
````
typedef enum  { 
  KsObjectTypeDevice         = 0,
  KsObjectTypeFilterFactory  = 1,
  KsObjectTypeFilter         = 2,
  KsObjectTypePin            = 3
} KSOBJECTTYPE;
````

## Constants

<table>

<tr>
<td>KsObjectTypeDevice</td>
<td>Specifies that the object is a device.</td>
</tr>

<tr>
<td>KsObjectTypeFilter</td>
<td>Specifies that the object is a filter.</td>
</tr>

<tr>
<td>KsObjectTypeFilterFactory</td>
<td>Specifies that the object is a filter factory.</td>
</tr>

<tr>
<td>KsObjectTypePin</td>
<td>Specifies that the object is a pin.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h (include Ks.h) |

## See Also

<dl>
<dt>
<a href="..\ks\nf-ks-ksgetobjecttypefromfileobject.md">KsGetObjectTypeFromFileObject</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksgetobjectfromfileobject.md">KsGetObjectFromFileObject</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksgetfilterfromfileobject.md">KsGetFilterFromFileObject</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksgetpinfromfileobject.md">KsGetPinFromFileObject</a>
</dt>
<dt>
<a href="..\ks\nf-ks-kspingetconnectedpinfileobject.md">KsPinGetConnectedPinFileObject</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSOBJECTTYPE enumeration%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
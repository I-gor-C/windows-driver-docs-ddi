---
UID : NF:wdm.FIELD_OFFSET
title : FIELD_OFFSET macro
author : windows-driver-content
description : The FIELD_OFFSET macro returns the byte offset of a named field in a known structure type.
old-location : kernel\field_offset.htm
old-project : kernel
ms.assetid : c792d021-3c64-4341-878c-08a7e163447c
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : k106_d6f0b450-e99c-4dd7-94c5-f428e4b1d642.xml, FIELD_OFFSET function [Kernel-Mode Driver Architecture], FIELD_OFFSET, kernel.field_offset, ntdef/FIELD_OFFSET
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : macro
req.header : wdm.h
req.include-header : Wdm.h, Ntddk.h
req.target-type : Desktop
req.target-min-winverclnt : Available starting with Windows 2000.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : wdm.h
req.dll : 
req.irql : Any level
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WORK_QUEUE_TYPE
req.product : Windows 10 or later.
---


# FIELD_OFFSET function
The <b>FIELD_OFFSET</b> macro returns the byte offset of a named field in a known structure type.

## Syntax

````
LONG FIELD_OFFSET(
  _In_ TYPE  Type,
  _In_ PCHAR Field
);
````

## Parameters

`type`

TBD

`field`

TBD


## Return Value

None

## Remarks

Used by device driver writers to symbolically determine the offset of a known field in a known structure type.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wdm.h (include Wdm.h, Ntddk.h) |
| **Library** |  |
| **IRQL** | Any level |
| **DDI compliance rules** |  |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff542043">CONTAINING_RECORD</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20FIELD_OFFSET function%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
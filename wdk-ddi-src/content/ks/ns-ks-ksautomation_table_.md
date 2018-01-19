---
UID : NS:ks.KSAUTOMATION_TABLE_
title : KSAUTOMATION_TABLE_
author : windows-driver-content
description : The KSAUTOMATION_TABLE structure defines a structure that combines tables for properties, methods, and events.
old-location : stream\ksautomation_table.htm
old-project : stream
ms.assetid : 76ab776d-0921-4fdb-9646-2cb97a582f6e
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KSAUTOMATION_TABLE_, *PKSAUTOMATION_TABLE, KSAUTOMATION_TABLE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ks.h
req.include-header : Ks.h
req.target-type : Windows
req.target-min-winverclnt : Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : KSAUTOMATION_TABLE
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
req.typenames : "*PKSAUTOMATION_TABLE, KSAUTOMATION_TABLE"
---

# KSAUTOMATION_TABLE_ structure
The KSAUTOMATION_TABLE structure defines a structure that combines tables for properties, methods, and events.

## Syntax
````
typedef struct KSAUTOMATION_TABLE_ {
  ULONG                PropertySetsCount;
  ULONG                PropertyItemSize;
  const KSPROPERTY_SET *PropertySets;
  ULONG                MethodSetsCount;
  ULONG                MethodItemSize;
  const KSMETHOD_SET   *MethodSets;
  ULONG                EventSetsCount;
  ULONG                EventItemSize;
  const KSEVENT_SET    *EventSets;
  PVOID                Alignment;
} KSAUTOMATION_TABLE, *PKSAUTOMATION_TABLE;
````

## Members


    ## Remarks
        Note that each object (pin, filter, topology node) should define an automation table. Minidrivers can use macros defined in <i>Ks.h</i> to define automation tables and the arrays they contain:

DEFINE_KSAUTOMATION_TABLE

DEFINE_KSAUTOMATION_PROPERTIES

DEFINE_KSAUTOMATION_METHODS

DEFINE_KSAUTOMATION_EVENTS

To specify an automation table containing an empty property array, event array, or method array:

DEFINE_KSAUTOMATION_PROPERTIES_NULL

DEFINE_KSAUTOMATION_METHODS_NULL

DEFINE_KSAUTOMATION_EVENTS_NULL

For example:

};

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
<a href="..\ks\ns-ks-ksproperty_set.md">KSPROPERTY_SET</a>
</dt>
<dt>
<a href="..\ks\ns-ks-ksmethod_set.md">KSMETHOD_SET</a>
</dt>
<dt>
<a href="..\ks\ns-ks-ksevent_set.md">KSEVENT_SET</a>
</dt>
<dt>
<a href="..\ks\ns-ks-ksproperty_item.md">KSPROPERTY_ITEM</a>
</dt>
<dt>
<a href="..\ks\ns-ks-ksmethod_item.md">KSMETHOD_ITEM</a>
</dt>
<dt>
<a href="..\ks\ns-ks-ksevent_item.md">KSEVENT_ITEM</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSAUTOMATION_TABLE structure%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
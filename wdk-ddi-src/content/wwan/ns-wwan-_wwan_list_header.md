---
UID: NS:wwan._WWAN_LIST_HEADER
title: "_WWAN_LIST_HEADER"
author: windows-driver-content
description: The WWAN_LIST_HEADER structure represents the header of a list of MB objects, including the number of objects in the list that follow the header in memory.
old-location: netvista\wwan_list_header.htm
old-project: netvista
ms.assetid: ef5c94e9-641c-41ea-baf1-343b876c92a4
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: "*PWWAN_LIST_HEADER, PWWAN_LIST_HEADER, PWWAN_LIST_HEADER structure pointer [Network Drivers Starting with Windows Vista], WWAN_LIST_HEADER, WWAN_LIST_HEADER structure [Network Drivers Starting with Windows Vista], WwanRef_78070f1a-5913-41b6-9be2-0b26c19dd149.xml, _WWAN_LIST_HEADER, netvista.wwan_list_header, wwan/PWWAN_LIST_HEADER, wwan/WWAN_LIST_HEADER"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
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
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wwan.h
api_name:
-	WWAN_LIST_HEADER
product: Windows
targetos: Windows
req.typenames: WWAN_LIST_HEADER, *PWWAN_LIST_HEADER
req.product: Windows 10 or later.
---

# _WWAN_LIST_HEADER structure
The WWAN_LIST_HEADER structure represents the header of a list of MB objects, including the number of
  objects in the list that follow the header in memory.

## Syntax
````
typedef struct _WWAN_LIST_HEADER {
  WWAN_STRUCT_TYPE ElementType;
  ULONG            ElementCount;
} WWAN_LIST_HEADER, *PWWAN_LIST_HEADER;
````

## Members


`ElementType`

A value from the 
     <a href="..\wwan\ne-wwan-_wwan_struct_type.md">WWAN_STRUCT_TYPE</a> enumeration that represents
     the type of objects in the list.

`ElementCount`

The number of elements in the list. The MB Service uses this information to allocate and
     reallocate memory for the list.

## Remarks
You can assume that the list of elements is stored in memory immediately following the data structure
    that contains the list.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 7 and later versions of Windows. Available in Windows 7 and later versions of Windows. |
| **Header** | wwan.h (include Wwan.h) |

## See Also

<a href="..\ndiswwan\ns-ndiswwan-_ndis_wwan_preferred_providers.md">NDIS_WWAN_PREFERRED_PROVIDERS</a>



<a href="..\ndiswwan\ns-ndiswwan-_ndis_wwan_set_preferred_providers.md">
   NDIS_WWAN_SET_PREFERRED_PROVIDERS</a>



<a href="..\ndiswwan\ns-ndiswwan-_ndis_wwan_sms_receive.md">NDIS_WWAN_SMS_RECEIVE</a>



<a href="..\wwan\ne-wwan-_wwan_struct_type.md">WWAN_STRUCT_TYPE</a>



<a href="..\ndiswwan\ns-ndiswwan-_ndis_wwan_provisioned_contexts.md">
   NDIS_WWAN_PROVISIONED_CONTEXTS</a>



<a href="..\ndiswwan\ns-ndiswwan-_ndis_wwan_visible_providers.md">NDIS_WWAN_VISIBLE_PROVIDERS</a>
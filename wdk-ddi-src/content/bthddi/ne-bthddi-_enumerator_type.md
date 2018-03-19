---
UID: NE:bthddi._ENUMERATOR_TYPE
title: "_ENUMERATOR_TYPE"
author: windows-driver-content
description: The ENUMERATOR_TYPE enumeration type is used to determine whether the enumerated device is associated with a service or a protocol. The ENUMERATOR_TYPE enumeration is intended for internal use only and should not be used by profile drivers.
old-location: bltooth\enumerator_type.htm
old-project: bltooth
ms.assetid: 2f8ae260-3a4c-44a5-85b7-e3ebcf21522b
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: "*PENUMERATOR_TYPE, ENUMERATOR_TYPE, ENUMERATOR_TYPE enumeration [Bluetooth Devices], ENUMERATOR_TYPE_MAX, ENUMERATOR_TYPE_PROTOCOL, ENUMERATOR_TYPE_SERVICE, PENUMERATOR_TYPE, PENUMERATOR_TYPE enumeration pointer [Bluetooth Devices], _ENUMERATOR_TYPE, bltooth.enumerator_type, bth_enums_48fc8cf9-53b6-46fd-831a-f4a5c56ff3f1.xml, bthddi/ENUMERATOR_TYPE, bthddi/ENUMERATOR_TYPE_MAX, bthddi/ENUMERATOR_TYPE_PROTOCOL, bthddi/ENUMERATOR_TYPE_SERVICE, bthddi/PENUMERATOR_TYPE"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: bthddi.h
req.include-header: Bthddi.h
req.target-type: Windows
req.target-min-winverclnt: Versions:\_Supported in Windows Vista, and later.
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
req.irql: Developers should code this function to operate at either IRQL = DISPATCH_LEVEL (if the callback   function does not access paged memory), or IRQL = PASSIVE_LEVEL (if the callback function must access   paged memory)
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	bthddi.h
api_name:
-	ENUMERATOR_TYPE
product: Windows
targetos: Windows
req.typenames: ENUMERATOR_TYPE, *PENUMERATOR_TYPE
---

# _ENUMERATOR_TYPE Enumeration
The ENUMERATOR_TYPE enumeration type is used to determine whether the enumerated device is associated
  with a service or a protocol. The ENUMERATOR_TYPE enumeration is intended for internal use only and should
  not be used by profile drivers.

## Syntax
````
typedef enum _ENUMERATOR_TYPE { 
  ENUMERATOR_TYPE_PROTOCOL  = 0,
  ENUMERATOR_TYPE_SERVICE   = 1,
  ENUMERATOR_TYPE_MAX       = 2
} ENUMERATOR_TYPE, *PENUMERATOR_TYPE;
````

## Constants

<table>
            
                <tr>
                    <td>ENUMERATOR_TYPE_PROTOCOL</td>
                    <td>For internal use only. Do not use.</td>
                </tr>
            
                <tr>
                    <td>ENUMERATOR_TYPE_SERVICE</td>
                    <td>This value should be specified for profile drivers. For more information about how this value is
     used, see 
     <a href="..\bthddi\ns-bthddi-_bth_enumerator_info.md">BTH_ENUMERATOR_INFO</a>.</td>
                </tr>
            
                <tr>
                    <td>ENUMERATOR_TYPE_DEVICE</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>ENUMERATOR_TYPE_MAX</td>
                    <td>For internal use only. Do not use.</td>
                </tr>
</table>

## Remarks

A value from this enumeration is returned as the 
    <b>EnumeratorType</b> member of the 
    <a href="..\bthddi\ns-bthddi-_bth_enumerator_info.md">BTH_ENUMERATOR_INFO</a> structure, which the 
    <a href="..\bthioctl\ni-bthioctl-ioctl_internal_bthenum_get_enuminfo.md">
    IOCTL_INTERNAL_BTHENUM_GET_ENUMINFO</a> returns in its output buffer.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Versions:\_Supported in Windows Vista, and later. Versions:\_Supported in Windows Vista, and later. |
| **Header** | bthddi.h (include Bthddi.h) |

## See Also

<a href="..\bthddi\ns-bthddi-_bth_enumerator_info.md">BTH_ENUMERATOR_INFO</a>



<a href="..\bthioctl\ni-bthioctl-ioctl_internal_bthenum_get_enuminfo.md">
   IOCTL_INTERNAL_BTHENUM_GET_ENUMINFO</a>
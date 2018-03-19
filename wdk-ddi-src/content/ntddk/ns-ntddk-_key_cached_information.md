---
UID: NS:ntddk._KEY_CACHED_INFORMATION
title: "_KEY_CACHED_INFORMATION"
author: windows-driver-content
description: The KEY_CACHED_INFORMATION structure holds the cached information available for a registry key or subkey.
old-location: kernel\key_cached_information.htm
old-project: kernel
ms.assetid: 5ee72ae9-0548-480f-84de-4c09ae4be507
ms.author: windowsdriverdev
ms.date: 3/1/2018
ms.keywords: "*PKEY_CACHED_INFORMATION, KEY_CACHED_INFORMATION, KEY_CACHED_INFORMATION structure [Kernel-Mode Driver Architecture], PKEY_CACHED_INFORMATION, PKEY_CACHED_INFORMATION structure pointer [Kernel-Mode Driver Architecture], _KEY_CACHED_INFORMATION, kernel.key_cached_information, kstruct_c_72dd8fcc-4983-49e0-af00-57b8fbbf3964.xml, ntddk/KEY_CACHED_INFORMATION, ntddk/PKEY_CACHED_INFORMATION"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating system.
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ntddk.h
api_name:
-	KEY_CACHED_INFORMATION
product: Windows
targetos: Windows
req.typenames: KEY_CACHED_INFORMATION, *PKEY_CACHED_INFORMATION
---

# _KEY_CACHED_INFORMATION structure
The <b>KEY_CACHED_INFORMATION</b> structure holds the cached information available for a registry key or subkey.

## Syntax
````
typedef struct _KEY_CACHED_INFORMATION {
  LARGE_INTEGER LastWriteTime;
  ULONG         TitleIndex;
  ULONG         SubKeys;
  ULONG         MaxNameLen;
  ULONG         Values;
  ULONG         MaxValueNameLen;
  ULONG         MaxValueDataLen;
  ULONG         NameLength;
} KEY_CACHED_INFORMATION, *PKEY_CACHED_INFORMATION;
````

## Members


`LastWriteTime`

The last time the key or any of its values changed. This time value is expressed in absolute system time format. Absolute system time is the number of 100-nanosecond intervals since the start of the year 1601 in the Gregorian calendar.

`TitleIndex`

Device and intermediate drivers should ignore this member.

`SubKeys`

The number of subkeys for a key.

`MaxNameLen`

The maximum number of bytes for a subkey name.

`Values`

The number of value entries.

`MaxValueNameLen`

The maximum length, in bytes, of any value entry name.

`MaxValueDataLen`

The maximum length, in bytes, of a value entry data field.

`NameLength`

The size, in bytes, of the key name.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating system. Available in Windows Vista and later versions of the Windows operating system. |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="..\wdm\ns-wdm-_key_full_information.md">KEY_FULL_INFORMATION</a>



<a href="..\wdm\ns-wdm-_key_basic_information.md">KEY_BASIC_INFORMATION</a>



<a href="..\ntddk\ns-ntddk-_key_virtualization_information.md">KEY_VIRTUALIZATION_INFORMATION</a>



<a href="..\wdm\ns-wdm-_key_node_information.md">KEY_NODE_INFORMATION</a>



<a href="..\wdm\nf-wdm-zwenumeratekey.md">ZwEnumerateKey</a>



<a href="..\wdm\ne-wdm-_key_information_class.md">KEY_INFORMATION_CLASS</a>



<a href="..\wdm\nf-wdm-zwquerykey.md">ZwQueryKey</a>



<a href="..\ntddk\ns-ntddk-_key_name_information.md">KEY_NAME_INFORMATION</a>
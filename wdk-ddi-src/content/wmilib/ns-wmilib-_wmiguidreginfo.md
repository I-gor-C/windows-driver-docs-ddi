---
UID : NS:wmilib._WMIGUIDREGINFO
title : _WMIGUIDREGINFO
author : windows-driver-content
description : The WMIGUIDREGINFO structure contains registration information for a given data block or event block exposed by a driver that uses the WMI library support routines.
old-location : kernel\wmiguidreginfo.htm
old-project : kernel
ms.assetid : 8bf36e54-5caa-4dc6-b659-ea0c1ac450f0
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : WMIGUIDREGINFO, PWMIGUIDREGINFO, wmilib/WMIGUIDREGINFO, WMIGUIDREGINFO structure [Kernel-Mode Driver Architecture], kernel.wmiguidreginfo, kstruct_d_aeedb315-3e08-4af9-9a37-afd06166a662.xml, PWMIGUIDREGINFO structure pointer [Kernel-Mode Driver Architecture], _WMIGUIDREGINFO, wmilib/PWMIGUIDREGINFO, *PWMIGUIDREGINFO
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : wmilib.h
req.include-header : Wmilib.h
req.target-type : Windows
req.target-min-winverclnt : 
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
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL (see Remarks section)
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WMIGUIDREGINFO, *PWMIGUIDREGINFO
req.product : Windows 10 or later.
---

# _WMIGUIDREGINFO structure
The <b>WMIGUIDREGINFO</b> structure contains registration information for a given data block or event block exposed by a driver that uses the WMI library support routines.

## Syntax
````
typedef struct _WMIGUIDREGINFO {
  LPCGUID Guid;
  ULONG   InstanceCount;
  ULONG   Flags;
} WMIGUIDREGINFO, *PWMIGUIDREGINFO;
````

## Members


`Flags`

Flag bits that indicate characteristics of the block. These flag bits are defined in the Wmistr.h header file. WMI ORs the <b>Flags</b> parameter value with the flag bits set by the driver in the <i>RegFlags</i> parameter of its <a href="..\wmilib\nc-wmilib-wmi_query_reginfo_callback.md">DpWmiQueryReginfo</a> routine, which apply to all of the data blocks and event blocks registered by the driver. <b>Flags</b> therefore supplements the driver's default settings for a given block.

A driver might set the following flag bit in <b>Flags</b>:



A driver might also set one or more of the following flag bits:

`Guid`

Pointer to the GUID that identifies the block. The memory that contains the GUID can be paged unless it is also used to call <a href="..\wmilib\nf-wmilib-wmifireevent.md">WmiFireEvent</a>.

`InstanceCount`

Specifies the number of instances defined for the block.

## Remarks
A driver that handles WMI IRPs by calling WMI library support routines builds an array of <b>WMIGUIDREGINFO</b> structures, one for each data block and event block to be registered. The driver sets the <b>GuidList</b> member of its <a href="..\wmilib\ns-wmilib-_wmilib_context.md">WMILIB_CONTEXT</a> structure to point to the first <b>WMIGUIDREGINFO</b> in the series.

Memory for this structure can be allocated from paged pool.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wmilib.h (include Wmilib.h) |

## See Also

<a href="..\wmilib\nc-wmilib-wmi_query_reginfo_callback.md">DpWmiQueryReginfo</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff551734">IRP_MN_REGINFO_EX</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550857">IRP_MN_ENABLE_COLLECTION</a>

<a href="..\wmilib\ns-wmilib-_wmilib_context.md">WMILIB_CONTEXT</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff551731">IRP_MN_REGINFO</a>

<a href="..\wmilib\nf-wmilib-wmifireevent.md">WmiFireEvent</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550848">IRP_MN_DISABLE_COLLECTION</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20WMIGUIDREGINFO structure%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
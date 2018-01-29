---
UID : NS:wmistr.WMIREGGUIDW
title : WMIREGGUIDW
author : windows-driver-content
description : The WMIREGGUID structure contains new or updated registration information for a data block or event block.
old-location : kernel\wmiregguid.htm
old-project : kernel
ms.assetid : f9f240ea-5689-4d33-8da7-b1cb7e66bc5b
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : PWMIREGGUID structure pointer [Kernel-Mode Driver Architecture], kstruct_d_1e7b2ada-5e56-42ed-bd0a-ec9bf25796f2.xml, wmistr/PWMIREGGUID, PWMIREGGUID, WMIREGGUIDW structure [Kernel-Mode Driver Architecture], WMIREGGUID, kernel.wmiregguid, wmistr/WMIREGGUID, *PWMIREGGUIDW, WMIREGGUIDW, WMIREGGUID structure [Kernel-Mode Driver Architecture]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : wmistr.h
req.include-header : Wmistr.h
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
req.typenames : WMIREGGUIDW, *PWMIREGGUIDW
req.product : Windows 10 or later.
---

# WMIREGGUIDW structure
The <b>WMIREGGUID</b> structure contains new or updated registration information for a data block or event block.

## Syntax
````
typedef struct {
  GUID  Guid;
  ULONG Flags;
  ULONG InstanceCount;
  union {
    ULONG     InstanceNameList;
    ULONG     BaseNameOffset;
    ULONG_PTR Pdo;
    ULONG_PTR InstanceInfo;
  };
} WMIREGGUID, *PWMIREGGUID;
````

## Members


`DUMMYUNIONNAME`



`Flags`

Indicates characteristics of the block to register or update. 

If a block is being registered with static instance names, a driver sets one of the following flags:



If a block is being registered with dynamic instance names, WMIREG_FLAG_INSTANCE_LIST, WMIREG_FLAG_INSTANCE_BASENAME, and WMIREG_FLAG_INSTANCE_PDO must be clear.

A driver might also set one or more of the following flags:

`Guid`

Specifies the GUID that represents the block to register or update.

`InstanceCount`

Specifies the number of static instance names to be defined for this block. If the block is being registered with dynamic instance names, WMI ignores <b>InstanceCount</b>.

## Remarks
A driver builds one or more <b>WMIREGGUID</b> structures in response to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551731">IRP_MN_REGINFO</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff551734">IRP_MN_REGINFO_EX</a> request to register or update its blocks. The driver passes an array of such structures at the <b>WmiRegGuid </b>member of a <b>WMIREGINFO</b> structure, which the driver writes to the buffer at <b>IrpStack-&gt;Parameters.WMI.Buffer</b>.

A driver can register or update a block with either static or dynamic instance names. Static instance names provide best performance; however, dynamic instance names are preferred for data blocks if the number of instances or instance names change frequently. For more information about instance names, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543029">Defining WMI Instance Names</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wmistr.h (include Wmistr.h) |

## See Also

<a href="..\wmistr\ns-wmistr-wmireginfow.md">WMIREGINFO</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff551734">IRP_MN_REGINFO_EX</a>

<a href="https://msdn.microsoft.com/library/windows/hardware/ff551731">IRP_MN_REGINFO</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20WMIREGGUIDW structure%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
---
UID : NF:wdm.IoWMISuggestInstanceName
title : IoWMISuggestInstanceName function
author : windows-driver-content
description : The IoWMISuggestInstanceName routine is used to request that WMI suggest a base name which a driver can use to build WMI instance names for the device.
old-location : kernel\iowmisuggestinstancename.htm
old-project : kernel
ms.assetid : a07ff2f6-e67e-489e-a477-6dc4b4ce6fed
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : k104_dc84cc9c-d6ca-40d2-93af-f54a149be7d1.xml, IoWMISuggestInstanceName, IoWMISuggestInstanceName routine [Kernel-Mode Driver Architecture], wdm/IoWMISuggestInstanceName, kernel.iowmisuggestinstancename
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : wdm.h
req.include-header : Wdm.h, Ntddk.h, Ntifs.h
req.target-type : Universal
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
req.lib : NtosKrnl.lib
req.dll : NtosKrnl.exe
req.irql : "<= APC_LEVEL"
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : WORK_QUEUE_TYPE
req.product : Windows 10 or later.
---


# IoWMISuggestInstanceName function
The <b>IoWMISuggestInstanceName</b> routine is used to request that WMI suggest a base name which a driver can use to build WMI instance names for the device.

## Syntax

````
NTSTATUS IoWMISuggestInstanceName(
  _In_opt_ PDEVICE_OBJECT  PhysicalDeviceObject,
  _In_opt_ PUNICODE_STRING SymbolicLinkName,
  _In_     BOOLEAN         CombineNames,
  _Out_    PUNICODE_STRING SuggestedInstanceName
);
````

## Parameters

`PhysicalDeviceObject`

If supplied, points to the driver's physical device object.

`SymbolicLinkName`

If supplied, points to the symbolic link name returned from <a href="..\wdm\nf-wdm-ioregisterdeviceinterface.md">IoRegisterDeviceInterface</a>.

`CombineNames`

If <b>TRUE</b> then the suggested names returned will combine the <i>PhysicalDeviceObject</i> and <i>SymbolicLinkName</i> information.

`SuggestedInstanceName`

A pointer to a buffer which upon successful completion will contain a <a href="..\wudfwdm\ns-wudfwdm-_unicode_string.md">UNICODE_STRING</a> which contains the suggested instance name. The caller is responsible for freeing this buffer when it is no longer needed.


## Return Value

<b>IoWMISuggestInstanceName</b> returns a status code from the following list:
<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
Indicates that WMI was able to successfully complete this function.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl>
</td>
<td width="60%">
Indicates that the WMI services are not available.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>
</td>
<td width="60%">
Indicates that insufficient resources were available to provide the caller with a buffer containing the Unicode string.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_NO_MEMORY</b></dt>
</dl>
</td>
<td width="60%">
Indicates that insufficient resources were available to provide the caller with a buffer containing the Unicode string.

</td>
</tr>
</table>

## Remarks

If the <i>CombineNames</i> parameter is <b>TRUE</b> then both <i>PhysicalDeviceObject</i> and <i>SymbolicLinkName</i> must be specified. Otherwise, only one of them should be specified.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 2000. Available starting with Windows 2000. |
| **Target Platform** | Universal |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<= APC_LEVEL" |

## See Also

<a href="..\wdm\nf-wdm-iowmiallocateinstanceids.md">IoWMIAllocateInstanceIds</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoWMISuggestInstanceName routine%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
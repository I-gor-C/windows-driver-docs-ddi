---
UID: NS.WDM._REG_DELETE_VALUE_KEY_INFORMATION
title: _REG_DELETE_VALUE_KEY_INFORMATION
author: windows-driver-content
description: The REG_DELETE_VALUE_KEY_INFORMATION structure contains information that a driver's RegistryCallback routine can use when a registry key's value is being deleted.
old-location: kernel\reg_delete_value_key_information.htm
old-project: kernel
ms.assetid: 7976ad9a-b40c-44b1-bc28-0bcb3b721e92
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _REG_DELETE_VALUE_KEY_INFORMATION, REG_DELETE_VALUE_KEY_INFORMATION, *PREG_DELETE_VALUE_KEY_INFORMATION, PREG_DELETE_VALUE_KEY_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available on Microsoft Windows XP and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: REG_DELETE_VALUE_KEY_INFORMATION
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
req.product: Windows 10 or later.
---

# _REG_DELETE_VALUE_KEY_INFORMATION structure



## -description
The <b>REG_DELETE_VALUE_KEY_INFORMATION</b> structure contains information that a driver's <a href="kernel.registrycallback">RegistryCallback</a> routine can use when a registry key's value is being deleted.



## -syntax

````
typedef struct _REG_DELETE_VALUE_KEY_INFORMATION {
  PVOID           Object;
  PUNICODE_STRING ValueName;
  PVOID           CallContext;
  PVOID           ObjectContext;
  PVOID           Reserved;
} REG_DELETE_VALUE_KEY_INFORMATION, *PREG_DELETE_VALUE_KEY_INFORMATION;
````


## -struct-fields

### -field Object

A pointer to the registry key object for the key whose value entry is about to be deleted.


### -field ValueName

A pointer to a <a href="kernel.unicode_string">UNICODE_STRING</a> structure that contains the name of the value entry that is about to be deleted.


### -field CallContext

Optional driver-defined context information that the driver's <a href="kernel.registrycallback">RegistryCallback</a> routine can supply. This member is defined for Windows Vista and later versions of the Windows operating system. 


### -field ObjectContext

A pointer to driver-defined context information that the driver has associated with a registry object by calling <a href="kernel.cmsetcallbackobjectcontext">CmSetCallbackObjectContext</a>. This member is defined for Windows Vista and later versions of the Windows operating system.


### -field Reserved

This member is reserved for future use. This member is defined for Windows Vista and later versions of the Windows operating system.


## -remarks
The system passes this structure to the <a href="kernel.registrycallback">RegistryCallback</a> routine every time a thread attempts to delete a value entry—for example, when a user-mode thread calls <b>RegDeleteValue</b> or when a driver calls <a href="kernel.zwdeletevaluekey">ZwDeleteValueKey</a>.

For more information about registry filtering operations, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545879">Filtering Registry Calls</a>.


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available on Microsoft Windows XP and later versions of the Windows operating system.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.cmsetcallbackobjectcontext">CmSetCallbackObjectContext</a>
</dt>
<dt>
<a href="kernel.registrycallback">RegistryCallback</a>
</dt>
<dt>
<a href="kernel.unicode_string">UNICODE_STRING</a>
</dt>
<dt>
<a href="kernel.zwdeletevaluekey">ZwDeleteValueKey</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20REG_DELETE_VALUE_KEY_INFORMATION structure%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


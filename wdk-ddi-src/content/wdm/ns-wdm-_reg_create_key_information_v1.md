---
UID: NS.WDM._REG_CREATE_KEY_INFORMATION_V1
title: _REG_CREATE_KEY_INFORMATION_V1
author: windows-driver-content
description: The REG_OPEN_KEY_INFORMATION_V1 structure contains information that a filter driver's RegistryCallback routine can use when a registry key is being opened.
old-location: kernel\reg_open_key_information_v1.htm
old-project: kernel
ms.assetid: 633463e5-7eec-44f5-99a3-bac43e216372
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _REG_CREATE_KEY_INFORMATION_V1, *PREG_CREATE_KEY_INFORMATION_V1, REG_CREATE_KEY_INFORMATION_V1, REG_OPEN_KEY_INFORMATION_V1, *PREG_OPEN_KEY_INFORMATION_V1
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available on Windows 7 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: REG_CREATE_KEY_INFORMATION_V1
req.alt-loc: wdm.h
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

# _REG_CREATE_KEY_INFORMATION_V1 structure



## -description
The <b>REG_OPEN_KEY_INFORMATION_V1</b> structure contains information that a filter driver's <a href="kernel.registrycallback">RegistryCallback</a> routine can use when a registry key is being opened.


## -syntax

````
typedef struct _REG_CREATE_KEY_INFORMATION_V1 {
  PUNICODE_STRING CompleteName;
  PVOID           RootObject;
  PVOID           ObjectType;
  ULONG           Options;
  PUNICODE_STRING Class;
  PVOID           SecurityDescriptor;
  PVOID           SecurityQualityOfService;
  ACCESS_MASK     DesiredAccess;
  ACCESS_MASK     GrantedAccess;
  PULONG          Disposition;
  PVOID           *ResultObject;
  PVOID           CallContext;
  PVOID           RootObjectContext;
  PVOID           Transaction;
  ULONG_PTR       Version;
  PUNICODE_STRING RemainingName;
  ULONG           Wow64Flags;
  ULONG           Attributes;
  KPROCESSOR_MODE CheckAccessMode;
} REG_CREATE_KEY_INFORMATION_V1, REG_OPEN_KEY_INFORMATION_V1, *PREG_CREATE_KEY_INFORMATION_V1, *PREG_OPEN_KEY_INFORMATION_V1;
````


## -struct-fields

### -field CompleteName

A pointer to a <a href="kernel.unicode_string">UNICODE_STRING</a> structure that contains the path of the new registry key. The path can be absolute or relative. If the path is absolute, this structure contains a fully qualified path that starts with the "\" character. For an absolute path, the <b>RootObject</b> member specifies the <b>\REGISTRY</b> key, which is the root directory of the registry tree. If the path is relative, the path starts with a character other than "\", and is relative to the key that is specified by the <b>RootObject</b> member. 

### -field RootObject

A pointer to a registry key object that represents the root registry key for the path that is specified by the <b>CompleteName</b> member. 

### -field ObjectType

This member is reserved for use by the operating system. Drivers must not access this member. 

### -field Options

Specifies the options for the key-open routine to use to create or open the new key. For more information, see the description of the <i>CreateOptions</i> parameter of the <a href="kernel.zwcreatekey">ZwCreateKey</a> routine and the description of the <i>OpenOptions</i> parameter of the <a href="kernel.zwopenkeyex">ZwOpenKeyEx</a> routine. 

### -field Class

This member is not used. 

### -field SecurityDescriptor

This member is not used. 

### -field SecurityQualityOfService

This member is not used. 

### -field DesiredAccess

The access mask that was specified by the thread that is trying to open the registry key. For more information about this access mask, see the description of the <i>DesiredAccess</i> parameter of the <a href="kernel.zwcreatekey">ZwCreateKey</a> routine. 

### -field GrantedAccess

An access mask that indicates the access rights that were granted to the thread that is trying to open the registry key. For more information about this member, see the following Remarks section. 

### -field Disposition

This member is not used. 

### -field ResultObject

A pointer to a location that receives the address of the key object that represents the opened registry key. 

### -field CallContext

A pointer to driver-defined context information that the driver has associated with a registry object by calling the <a href="kernel.cmsetcallbackobjectcontext">CmSetCallbackObjectContext</a> routine. 

### -field RootObjectContext

A pointer to driver-defined context information that the driver has associated with the root of the path of the registry object by calling the <a href="kernel.cmsetcallbackobjectcontext">CmSetCallbackObjectContext</a> routine. 

### -field Transaction

A pointer to a transaction object for the registry operation. You can supply this pointer to the <a href="ifsk.obopenobjectbypointer">ObOpenObjectByPointer</a> routine to obtain the corresponding transaction handle. If this member is <b>NULL</b>, the operation is being performed in non-transactional context. 

### -field Version

The structure version number. This member distinguishes the <a href="kernel.reg_open_key_information">REG_OPEN_KEY_INFORMATION</a> structure in Windows Vista from the <b>REG_OPEN_KEY_INFORMATION_V1</b> structure in Windows 7 and later versions of Windows. The following version numbers are currently defined.
<table>
<tr>
<th>Version number</th>
<th>Version of structure</th>
</tr>
<tr>
<td>
0
</td>
<td>
<b>REG_OPEN_KEY_INFORMATION</b>
</td>
</tr>
<tr>
<td>
1
</td>
<td>
<b>REG_OPEN_KEY_INFORMATION_V1</b>
</td>
</tr>
</table>
 
Future versions of this structure might add new members but will not change the members that are already defined in existing versions of the structure. This member is defined in the <b>REG_OPEN_KEY_INFORMATION_KEY_INFORMATION_V1</b> structure that is supported in Windows 7 and later versions of the Windows operating systems. In the <b>REG_OPEN_KEY_INFORMATION</b> structure that Windows Vista supports, this member is named <b>Reserved</b> and is set to zero. Filter drivers should rely on the version number and not the operating system version to determine which version of the structure they are using. 

### -field RemainingName

A pointer to a <a href="kernel.unicode_string">UNICODE_STRING</a> structure that contains the relative path of the new registry key. This member always expresses the path of the new key relative to the path of the key that is specified by the <b>RootObject</b> member. In contrast, the <b>CompleteName</b> member can contain an absolute path if the <b>RootObject</b> member specifies the <b>\REGISTRY</b> key. 

### -field Wow64Flags

Contains the Wow64 flags from the access mask that was passed as an input parameter in the call to open the new registry key. This member indicates whether a 32-bit client program that is running on a 64-bit version of Windows is trying to open a registry key. This member is set to zero or to one of the following flag bits:
<ul>
<li>
KEY_WOW64_32KEY
</li>
<li>
KEY_WOW64_64KEY
</li>
</ul>
These flag bits are defined in the Wdm.h and Winnt.h header files. For more information about these flags, see <a href="http://go.microsoft.com/fwlink/p/?linkid=155080">Registry Key Security and Access Rights</a>.

### -field Attributes

Contains the object-attribute flags from the <b>Attributes</b> member of the <a href="kernel.object_attributes">OBJECT_ATTRIBUTES</a> structure that was passed as an input parameter in the call to open the new registry key. This member might contain one or more of the following flag bits:
<ul>
<li>
OBJ_KERNEL_HANDLE
</li>
<li>
OBJ_FORCE_ACCESS_CHECK
</li>
<li>
OBJ_OPENLINK
</li>
</ul>
For more information about these flags, see <a href="kernel.object_attributes">OBJECT_ATTRIBUTES</a>.

### -field CheckAccessMode

Indicates how the configuration manager performs the security access check for the call to create the new key. This member contains one of the following <b>MODE</b> enumeration values from the Wdm.h header file:
<ul>
<li>
<b>KernelMode</b>
</li>
<li>
<b>UserMode</b>
</li>
</ul>
This security access check is similar to that performed by the <a href="kernel.seaccesscheck">SeAccessCheck</a> routine, which has an <i>AccessMode</i> parameter that can be set to either <b>KernelMode</b> or <b>UserMode</b>. If <b>CheckAccessMode</b> is set to <b>UserMode</b>, the configuration manager performs a full security access check regardless of whether the call originated in user mode or kernel mode. For more information about how to force user-mode security access checks on a call that originates in kernel mode, see the description of the OBJ_FORCE_ACCESS_CHECK flag in the <b>Attributes</b> member of the <b>OBJECT_ATTRIBUTES</b> structure. 

## -remarks
The configuration manager passes this structure to the <i>RegistryCallback</i> routine every time that a thread tries to open a key—for example, when a user-mode thread calls <a href="http://go.microsoft.com/fwlink/p/?linkid=155081">RegOpenKey</a> or <a href="http://go.microsoft.com/fwlink/p/?linkid=155082">RegOpenKeyEx</a>, or when a kernel-mode driver calls <a href="kernel.zwopenkey">ZwOpenKey</a>.

This structure is an extended version of the <a href="kernel.reg_open_key_information">REG_OPEN_KEY_INFORMATION</a> structure that Windows Vista supports. The first 14 members, <b>CompleteName</b> through <b>Transaction</b>, are identical in the two structures. The last five members of the <b>REG_OPEN_KEY_INFORMATION_V1</b> structure, <b>Version</b> through <b>CheckAccessMode</b>, are not part of the <b>REG_OPEN_KEY_INFORMATION</b> structure.

If the driver's <i>RegistryCallback</i> routine returns STATUS_CALLBACK_BYPASS for a <b>RegNtPreOpenKeyEx</b> notification, the driver must supply the values for the <b>GrantedAccess</b> and <b>ResultObject</b> members. 

The <b>REG_OPEN_KEY_INFORMATION_V1</b> structure is one of a number of structures that a filter driver can receive through its <i>RegistryCallback</i> routine. For more information about filter drivers, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545879">Filtering Registry Calls</a>.

For more information about registry filtering operations, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545879">Filtering Registry Calls</a>.

## -requirements
<table>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available on Windows 7 and later versions of the Windows operating systems.
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
<a href="kernel.object_attributes">OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="ifsk.obopenobjectbypointer">ObOpenObjectByPointer</a>
</dt>
<dt>
<a href="kernel.registrycallback">RegistryCallback</a>
</dt>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=155081">RegOpenKey</a></dt>
<dt>
<a href="kernel.reg_open_key_information">REG_OPEN_KEY_INFORMATION</a>
</dt>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=155082">RegOpenKeyEx</a></dt>
<dt>
<a href="kernel.unicode_string">UNICODE_STRING</a>
</dt>
<dt>
<a href="kernel.zwcreatekey">ZwCreateKey</a>
</dt>
<dt>
<a href="kernel.zwopenkeyex">ZwOpenKeyEx</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20REG_OPEN_KEY_INFORMATION_V1 structure%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

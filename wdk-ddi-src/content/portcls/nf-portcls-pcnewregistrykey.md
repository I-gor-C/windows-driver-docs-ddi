---
UID: NF.portcls.PcNewRegistryKey
title: PcNewRegistryKey
author: windows-driver-content
description: The PcNewRegistryKey function opens or creates a new registry key and creates an IRegistryKey object to represent the key. The caller accesses the key through this object.
old-location: audio\pcnewregistrykey.htm
old-project: audio
ms.assetid: d8ef9e7f-8ce0-48df-973f-170c47e55777
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PcNewRegistryKey
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: The PortCls system driver implements the PcNewRegistryKey function in Microsoft Windows 98/Me and in Windows 2000 and later operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PcNewRegistryKey
req.alt-loc: Portcls.lib,Portcls.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Portcls.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PcNewRegistryKey function



## -description
<p>The <b>PcNewRegistryKey</b> function opens or creates a new registry key and creates an <a href="..\portcls\nn-portcls-iregistrykey.md">IRegistryKey</a> object to represent the key. The caller accesses the key through this object.</p>


## -syntax

````
NTSTATUS PcNewRegistryKey(
  _Out_     PREGISTRYKEY       *OutRegistryKey,
  _In_opt_  PUNKNOWN           OuterUnknown,
  _In_      ULONG              RegistryKeyType,
  _In_      ACCESS_MASK        DesiredAccess,
  _In_opt_  PVOID              DeviceObject,
  _In_opt_  PVOID              SubDevice,
  _In_opt_  POBJECT_ATTRIBUTES ObjectAttributes,
  _In_opt_  ULONG              CreateOptions,
  _Out_opt_ PULONG             Disposition
);
````


## -parameters
<dl>

### -param OutRegistryKey [out]

<dd>
<p>Output pointer to the registry-key object created by this function. This parameter points to a caller-allocated pointer variable into which the function outputs the pointer to the <a href="..\portcls\nn-portcls-iregistrykey.md">IRegistryKey</a> object. The object represents the registry key being opened or created. Specify a valid, non-<b>NULL</b> pointer value for this parameter.</p>
</dd>

### -param OuterUnknown [in, optional]

<dd>
<p>Pointer to the <a href="com.iunknown">IUnknown</a> interface of an object that needs to aggregate the <i>OutRegistryKey</i> object. Unless aggregation is required, set this parameter to <b>NULL</b>.</p>
</dd>

### -param RegistryKeyType [in]

<dd>
<p>Specifies the type of registry key that the caller wants to create or open. For more information, see the following Remarks section.</p>
</dd>

### -param DesiredAccess [in]

<dd>
<p>Specifies an access-control mask. This parameter is a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>. It indicates the type of access that the caller is requesting to the registry key that is to be opened or created. For more information, see the following Remarks section.</p>
</dd>

### -param DeviceObject [in, optional]

<dd>
<p>Pointer to the adapter driver's device object. This pointer is cast to type PVOID. If <i>RegistryKeyType</i> is any value other than <b>GeneralRegistryKey</b>, this parameter must point to a valid, initialized system structure of type <a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a>. If the value of <i>RegistryKeyType</i> is <b>GeneralRegistryKey</b>, the <b>PcNewRegistryKey</b> function does not use this parameter. For more information, see the following Remarks section.</p>
</dd>

### -param SubDevice [in, optional]

<dd>
<p>Specifies the aspect of the device that is to be offered to clients. Adapter drivers must assign the value <b>NULL</b> to this parameter.</p>
</dd>

### -param ObjectAttributes [in, optional]

<dd>
<p>Pointer to the object attributes of the key being created or opened. If <i>RegistryKeyType</i> has the value <b>GeneralRegistryKey</b>, this parameter must point to a valid, initialized system structure of type <a href="..\d3dkmthk\ns-d3dkmthk--object-attributes.md">OBJECT_ATTRIBUTES</a> with a valid <i>ObjectName</i> string for the key; otherwise, the function does not use this parameter. For more information, see the following Remarks section.</p>
</dd>

### -param CreateOptions [in, optional]

<dd>
<p>Specifies the create options. Can be zero if none are desired. If <i>RegistryKeyType</i> is not <b>GeneralRegistryKey</b>, the <b>PcNewRegistryKey</b> function ignores this parameter. For more information, see the following Remarks section.</p>
</dd>

### -param Disposition [out, optional]

<dd>
<p>Pointer to a variable that receives a value indicating whether a key was created or an existing key was opened. This parameter is optional and can be specified as <b>NULL</b>. If <i>RegistryKeyType</i> is any value other than <b>GeneralRegistryKey</b>, the <b>PcNewRegistryKey</b> function ignores this parameter. For more information, see the following Remarks section.</p>
</dd>
</dl>

## -returns
<p><b>PcNewRegistryKey</b> returns STATUS_SUCCESS if the call was successful. Otherwise, it returns an appropriate error code.</p>

## -remarks
<p>If the <i>RegistryKeyType</i> parameter's value is <b>GeneralRegistryKey</b>, then the <b>PcNewRegistryKey</b> function either opens an existing key or creates a new key in the registry, as indicated by the value that the function outputs through the <i>Disposition</i> parameter. If the key is of any type other than <b>GeneralRegistryKey</b>, then the function opens an already existing key that was previously created during Plug and Play device enumeration.</p>

<p>The <i>DesiredAccess</i>, <i>ObjectAttributes</i>, <i>CreateOptions</i>, and <i>Disposition</i> parameters take on the values that are defined for the parameters with the same names in the <a href="..\wdm\nf-wdm-zwcreatekey.md">ZwCreateKey</a> call.</p>

<p>The <i>RegistryKeyType</i> parameter should be set to one of the enumeration values shown in the following table.</p>

<p><b>GeneralRegistryKey</b></p>

<p>Provide generic access to any key type. Open the specified key if it already exists or create the key if it does not.</p>

<p><b>DeviceRegistryKey</b></p>

<p>Open an existing key containing device-specific information. The key is located under the key for the device instance specified by <i>DeviceObject</i>.</p>

<p><b>DriverRegistryKey</b></p>

<p>Open an existing key containing driver-specific information.</p>

<p><b>HwProfileRegistryKey</b></p>

<p>Open an existing key relative to the current hardware profile containing device or driver information. This allows the driver to access configuration information that is hardware-profile-specific.</p>

<p><b>DeviceInterfaceRegistryKey</b></p>

<p>Not used with <b>PcNewRegistryKey</b>. See <a href="audio.iport_newregistrykey">IPort::NewRegistryKey</a> for details.</p>

<p>For a <i>RegistryKeyType</i> value of <b>GeneralRegistryKey</b>, the caller must provide a valid <i>ObjectAttributes</i> parameter value, and the <i>CreateOptions</i> and <i>Disposition</i> parameters are optional. For any other <i>RegistryKeyType</i> value, the caller must provide a valid <i>DeviceObject</i> parameter value, and the <i>CreateOptions</i> and <i>Disposition</i> parameters are not used.</p>

<p>The <i>ObjectAttributes</i> parameter points to an opaque structure of type OBJECT_ATTRIBUTES that contains object attributes such as key name and security descriptor. Use the <a href="..\wudfwdm\nf-wudfwdm-initializeobjectattributes.md">InitializeObjectAttributes</a> macro to initialize the structure. In the <i>Attributes</i> parameter for this macro, set the OBJ_KERNEL_HANDLE flag unless you intend to allow non-secure, user-mode applications to have read/write access to the registry key.</p>

<p>The <i>DesiredAccess</i> parameter is an access-control mask. It specifies the type of access control that the caller needs to have to the new registry key when accessing it through the <i>OutRegistryKey</i> object. This mask should not be confused with the access control list (ACL) that controls access by users to the registry key. When calling <b>PcNewRegistryKey</b> to create a registry key of type <b>GeneralRegistryKey</b>, the <i>ObjectAttributes </i>parameter specifies the key's attributes, including a security descriptor that contains the ACL. However, if the new key is of type <b>GeneralRegistryKey</b> and either the security descriptor pointer in the <i>ObjectAttributes </i>structure is <b>NULL</b> or the ACL pointer in the security descriptor is <b>NULL</b>, then the new key will inherit the parent key's ACL by default.</p>

<p>If the key is of any type other than <b>GeneralRegistryKey</b>, then the key retains the ACL that Plug and Play assigned to the key when it was created during device enumeration.</p>

<p>The <b>PcNewRegistryKey</b> function is similar to the <a href="audio.iport_newregistrykey">IPort::NewRegistryKey</a> method except that the device object and port object must be explicitly specified in a <b>PcNewRegistryKey</b> call but are simply implied in a <b>NewRegistryKey</b> call. <b>PcNewRegistryKey</b> is used primarily by adapter drivers. Miniport drivers typically call <b>NewRegistryKey</b> instead.</p>

<p>The <i>OutRegistryKey</i> and <i>OuterUnknown</i> parameters follow the <a href="https://msdn.microsoft.com/e6b19110-37e2-4d23-a528-6393c12ab650">reference-counting conventions for COM objects</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>The PortCls system driver implements the PcNewRegistryKey function in Microsoft Windows 98/Me and in Windows 2000 and later operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\portcls\nn-portcls-iregistrykey.md">IRegistryKey</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a>
</dt>
<dt>
<a href="..\d3dkmthk\ns-d3dkmthk--object-attributes.md">OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwcreatekey.md">ZwCreateKey</a>
</dt>
<dt>
<a href="..\wudfwdm\nf-wudfwdm-initializeobjectattributes.md">InitializeObjectAttributes</a>
</dt>
<dt>
<a href="audio.iport_newregistrykey">IPort::NewRegistryKey</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PcNewRegistryKey function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

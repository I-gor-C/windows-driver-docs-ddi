---
UID: NE.wdm.DEVICE_REGISTRY_PROPERTY
title: DEVICE_REGISTRY_PROPERTY
author: windows-driver-content
description: The DEVICE_REGISTRY_PROPERTY enumeration identifies device properties that are stored in the registry.
old-location: kernel\device_registry_property.htm
old-project: kernel
ms.assetid: a17b4a88-45e8-45e7-b879-2f41b97be368
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEVICE_REGISTRY_PROPERTY
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
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# DEVICE_REGISTRY_PROPERTY enumeration



## -description
<p>The <b>DEVICE_REGISTRY_PROPERTY</b> enumeration identifies device properties that are stored in the registry.</p>


## -syntax

````
typedef enum  { 
  DevicePropertyDeviceDescription            = 0x0,
  DevicePropertyHardwareID                   = 0x1,
  DevicePropertyCompatibleIDs                = 0x2,
  DevicePropertyBootConfiguration            = 0x3,
  DevicePropertyBootConfigurationTranslated  = 0x4,
  DevicePropertyClassName                    = 0x5,
  DevicePropertyClassGuid                    = 0x6,
  DevicePropertyDriverKeyName                = 0x7,
  DevicePropertyManufacturer                 = 0x8,
  DevicePropertyFriendlyName                 = 0x9,
  DevicePropertyLocationInformation          = 0xa,
  DevicePropertyPhysicalDeviceObjectName     = 0xb,
  DevicePropertyBusTypeGuid                  = 0xc,
  DevicePropertyLegacyBusType                = 0xd,
  DevicePropertyBusNumber                    = 0xe,
  DevicePropertyEnumeratorName               = 0xf,
  DevicePropertyAddress                      = 0x10,
  DevicePropertyUINumber                     = 0x11,
  DevicePropertyInstallState                 = 0x12,
  DevicePropertyRemovalPolicy                = 0x13,
  DevicePropertyResourceRequirements         = 0x14,
  DevicePropertyAllocatedResources           = 0x15,
  DevicePropertyContainerID                  = 0x16
} DEVICE_REGISTRY_PROPERTY;
````


## -enum-fields
<dl>

### -field <a id="DevicePropertyDeviceDescription"></a><a id="devicepropertydevicedescription"></a><a id="DEVICEPROPERTYDEVICEDESCRIPTION"></a><b>DevicePropertyDeviceDescription</b>

<dd></dd>

### -field <a id="DevicePropertyHardwareID"></a><a id="devicepropertyhardwareid"></a><a id="DEVICEPROPERTYHARDWAREID"></a><b>DevicePropertyHardwareID</b>

<dd></dd>

### -field <a id="DevicePropertyCompatibleIDs"></a><a id="devicepropertycompatibleids"></a><a id="DEVICEPROPERTYCOMPATIBLEIDS"></a><b>DevicePropertyCompatibleIDs</b>

<dd></dd>

### -field <a id="DevicePropertyBootConfiguration"></a><a id="devicepropertybootconfiguration"></a><a id="DEVICEPROPERTYBOOTCONFIGURATION"></a><b>DevicePropertyBootConfiguration</b>

<dd></dd>

### -field <a id="DevicePropertyBootConfigurationTranslated"></a><a id="devicepropertybootconfigurationtranslated"></a><a id="DEVICEPROPERTYBOOTCONFIGURATIONTRANSLATED"></a><b>DevicePropertyBootConfigurationTranslated</b>

<dd></dd>

### -field <a id="DevicePropertyClassName"></a><a id="devicepropertyclassname"></a><a id="DEVICEPROPERTYCLASSNAME"></a><b>DevicePropertyClassName</b>

<dd></dd>

### -field <a id="DevicePropertyClassGuid"></a><a id="devicepropertyclassguid"></a><a id="DEVICEPROPERTYCLASSGUID"></a><b>DevicePropertyClassGuid</b>

<dd></dd>

### -field <a id="DevicePropertyDriverKeyName"></a><a id="devicepropertydriverkeyname"></a><a id="DEVICEPROPERTYDRIVERKEYNAME"></a><b>DevicePropertyDriverKeyName</b>

<dd></dd>

### -field <a id="DevicePropertyManufacturer"></a><a id="devicepropertymanufacturer"></a><a id="DEVICEPROPERTYMANUFACTURER"></a><b>DevicePropertyManufacturer</b>

<dd></dd>

### -field <a id="DevicePropertyFriendlyName"></a><a id="devicepropertyfriendlyname"></a><a id="DEVICEPROPERTYFRIENDLYNAME"></a><b>DevicePropertyFriendlyName</b>

<dd></dd>

### -field <a id="DevicePropertyLocationInformation"></a><a id="devicepropertylocationinformation"></a><a id="DEVICEPROPERTYLOCATIONINFORMATION"></a><b>DevicePropertyLocationInformation</b>

<dd></dd>

### -field <a id="DevicePropertyPhysicalDeviceObjectName"></a><a id="devicepropertyphysicaldeviceobjectname"></a><a id="DEVICEPROPERTYPHYSICALDEVICEOBJECTNAME"></a><b>DevicePropertyPhysicalDeviceObjectName</b>

<dd></dd>

### -field <a id="DevicePropertyBusTypeGuid"></a><a id="devicepropertybustypeguid"></a><a id="DEVICEPROPERTYBUSTYPEGUID"></a><b>DevicePropertyBusTypeGuid</b>

<dd></dd>

### -field <a id="DevicePropertyLegacyBusType"></a><a id="devicepropertylegacybustype"></a><a id="DEVICEPROPERTYLEGACYBUSTYPE"></a><b>DevicePropertyLegacyBusType</b>

<dd></dd>

### -field <a id="DevicePropertyBusNumber"></a><a id="devicepropertybusnumber"></a><a id="DEVICEPROPERTYBUSNUMBER"></a><b>DevicePropertyBusNumber</b>

<dd></dd>

### -field <a id="DevicePropertyEnumeratorName"></a><a id="devicepropertyenumeratorname"></a><a id="DEVICEPROPERTYENUMERATORNAME"></a><b>DevicePropertyEnumeratorName</b>

<dd></dd>

### -field <a id="DevicePropertyAddress"></a><a id="devicepropertyaddress"></a><a id="DEVICEPROPERTYADDRESS"></a><b>DevicePropertyAddress</b>

<dd></dd>

### -field <a id="DevicePropertyUINumber"></a><a id="devicepropertyuinumber"></a><a id="DEVICEPROPERTYUINUMBER"></a><b>DevicePropertyUINumber</b>

<dd></dd>

### -field <a id="DevicePropertyInstallState"></a><a id="devicepropertyinstallstate"></a><a id="DEVICEPROPERTYINSTALLSTATE"></a><b>DevicePropertyInstallState</b>

<dd></dd>

### -field <a id="DevicePropertyRemovalPolicy"></a><a id="devicepropertyremovalpolicy"></a><a id="DEVICEPROPERTYREMOVALPOLICY"></a><b>DevicePropertyRemovalPolicy</b>

<dd></dd>

### -field <a id="DevicePropertyResourceRequirements"></a><a id="devicepropertyresourcerequirements"></a><a id="DEVICEPROPERTYRESOURCEREQUIREMENTS"></a><b>DevicePropertyResourceRequirements</b>

<dd></dd>

### -field <a id="DevicePropertyAllocatedResources"></a><a id="devicepropertyallocatedresources"></a><a id="DEVICEPROPERTYALLOCATEDRESOURCES"></a><b>DevicePropertyAllocatedResources</b>

<dd></dd>

### -field <a id="DevicePropertyContainerID"></a><a id="devicepropertycontainerid"></a><a id="DEVICEPROPERTYCONTAINERID"></a><b>DevicePropertyContainerID</b>

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549203">IoGetDeviceProperty</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20DEVICE_REGISTRY_PROPERTY Enumeration enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

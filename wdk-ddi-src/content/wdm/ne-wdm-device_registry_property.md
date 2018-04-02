---
UID: NE:wdm.DEVICE_REGISTRY_PROPERTY
title: DEVICE_REGISTRY_PROPERTY
author: windows-driver-content
description: The DEVICE_REGISTRY_PROPERTY enumeration identifies device properties that are stored in the registry.
old-location: kernel\device_registry_property.htm
old-project: kernel
ms.assetid: a17b4a88-45e8-45e7-b879-2f41b97be368
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: DEVICE_REGISTRY_PROPERTY, DEVICE_REGISTRY_PROPERTY enumeration [Kernel-Mode Driver Architecture], DevicePropertyAddress, DevicePropertyAllocatedResources, DevicePropertyBootConfiguration, DevicePropertyBootConfigurationTranslated, DevicePropertyBusNumber, DevicePropertyBusTypeGuid, DevicePropertyClassGuid, DevicePropertyClassName, DevicePropertyCompatibleIDs, DevicePropertyContainerID, DevicePropertyDeviceDescription, DevicePropertyDriverKeyName, DevicePropertyEnumeratorName, DevicePropertyFriendlyName, DevicePropertyHardwareID, DevicePropertyInstallState, DevicePropertyLegacyBusType, DevicePropertyLocationInformation, DevicePropertyManufacturer, DevicePropertyPhysicalDeviceObjectName, DevicePropertyRemovalPolicy, DevicePropertyResourceRequirements, DevicePropertyUINumber, enumeration [Kernel-Mode Driver Architecture], kernel.device_registry_property, sysenum_485e3369-186a-4a71-b13e-be6ff9ab8dce.xml, wdm/, wdm/DevicePropertyAddress, wdm/DevicePropertyAllocatedResources, wdm/DevicePropertyBootConfiguration, wdm/DevicePropertyBootConfigurationTranslated, wdm/DevicePropertyBusNumber, wdm/DevicePropertyBusTypeGuid, wdm/DevicePropertyClassGuid, wdm/DevicePropertyClassName, wdm/DevicePropertyCompatibleIDs, wdm/DevicePropertyContainerID, wdm/DevicePropertyDeviceDescription, wdm/DevicePropertyDriverKeyName, wdm/DevicePropertyEnumeratorName, wdm/DevicePropertyFriendlyName, wdm/DevicePropertyHardwareID, wdm/DevicePropertyInstallState, wdm/DevicePropertyLegacyBusType, wdm/DevicePropertyLocationInformation, wdm/DevicePropertyManufacturer, wdm/DevicePropertyPhysicalDeviceObjectName, wdm/DevicePropertyRemovalPolicy, wdm/DevicePropertyResourceRequirements, wdm/DevicePropertyUINumber
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h, Wudfwdm.h
req.target-type: Windows
req.target-min-winverclnt: 
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
-	Wdm.h
api_name:
-	DEVICE_REGISTRY_PROPERTY
product:
- Windows
targetos: Windows
req.typenames: DEVICE_REGISTRY_PROPERTY
req.product: Windows 10 or later.
---

# DEVICE_REGISTRY_PROPERTY Enumeration
The <b>DEVICE_REGISTRY_PROPERTY</b> enumeration identifies device properties that are stored in the registry.

## Syntax
```
typedef enum DEVICE_REGISTRY_PROPERTY {
  DevicePropertyDeviceDescription            ,
  DevicePropertyHardwareID                   ,
  DevicePropertyCompatibleIDs                ,
  DevicePropertyBootConfiguration            ,
  DevicePropertyBootConfigurationTranslated  ,
  DevicePropertyClassName                    ,
  DevicePropertyClassGuid                    ,
  DevicePropertyDriverKeyName                ,
  DevicePropertyManufacturer                 ,
  DevicePropertyFriendlyName                 ,
  DevicePropertyLocationInformation          ,
  DevicePropertyPhysicalDeviceObjectName     ,
  DevicePropertyBusTypeGuid                  ,
  DevicePropertyLegacyBusType                ,
  DevicePropertyBusNumber                    ,
  DevicePropertyEnumeratorName               ,
  DevicePropertyAddress                      ,
  DevicePropertyUINumber                     ,
  DevicePropertyInstallState                 ,
  DevicePropertyRemovalPolicy                ,
  DevicePropertyResourceRequirements         ,
  DevicePropertyAllocatedResources           ,
  DevicePropertyContainerID
} ;
```

## Constants

<table>
            
                <tr>
                    <td>DevicePropertyDeviceDescription</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DevicePropertyHardwareID</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DevicePropertyCompatibleIDs</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DevicePropertyBootConfiguration</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DevicePropertyBootConfigurationTranslated</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DevicePropertyClassName</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DevicePropertyClassGuid</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DevicePropertyDriverKeyName</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DevicePropertyManufacturer</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DevicePropertyFriendlyName</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DevicePropertyLocationInformation</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DevicePropertyPhysicalDeviceObjectName</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DevicePropertyBusTypeGuid</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DevicePropertyLegacyBusType</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DevicePropertyBusNumber</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DevicePropertyEnumeratorName</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DevicePropertyAddress</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DevicePropertyUINumber</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DevicePropertyInstallState</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DevicePropertyRemovalPolicy</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DevicePropertyResourceRequirements</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DevicePropertyAllocatedResources</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>DevicePropertyContainerID</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h, Wudfwdm.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff549203">IoGetDeviceProperty</a>
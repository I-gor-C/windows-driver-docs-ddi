---
UID: NN:prcomoem.IPrintCoreUI2
title: IPrintCoreUI2
author: windows-driver-content
description: This section describes the methods defined for the IPrintCoreUI2 COM Interface.
old-location: print\iprintcoreui2_interface.htm
old-project: print
ms.assetid: e2d2e486-d69d-4a6d-aaab-a7b8806665b4
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IPrintCoreUI2, IPrintCoreUI2 interface [Print Devices], IPrintCoreUI2 interface [Print Devices], described, prcomoem/IPrintCoreUI2, print.iprintcoreui2_interface, print_unidrv-pscript_ui_e96a2262-fab6-4128-b312-90fde72006e0.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: prcomoem.h
req.include-header: 
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
req.lib: prcomoem.h
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	prcomoem.h
api_name:
-	IPrintCoreUI2
product: Windows
targetos: Windows
req.typenames: OEMPTOPTS, *POEMPTOPTS
req.product: Windows 10 or later.
---

# IPrintCoreUI2 interface

This section describes the methods defined for the <a href="https://msdn.microsoft.com/3c9df0ac-d823-4c27-bd34-85765f48b972">IPrintCoreUI2 COM Interface</a>.

This interface inherits from the <a href="https://msdn.microsoft.com/ed11789f-750d-4f29-b5e0-ab299a1388db">IPrintOemDriverUI COM Interface</a>. The methods in this interface are provided by the Windows XP Pscript5 driver, for the sole use of its user interface plug-ins. Method prototypes appear in prcomoem.h.

## Methods

<p>The <b>IPrintCoreUI2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintCoreUI2::DrvGetDriverSetting](nf-prcomoem-iprintcoreui2-drvgetdriversetting.md) | The IPrintCoreUI2::DrvGetDriverSetting method is provided by the Windows XP Pscript5 driver so that Pscript5 user interface plug-ins can obtain the current status of printer features and other internal information. |
| [IPrintCoreUI2::DrvUpdateUISetting](nf-prcomoem-iprintcoreui2-drvupdateuisetting.md) | The IPrintCoreUI2::DrvUpdateUISetting method is provided by the Windows XP Pscript5 driver so that Pscript5 user interface plug-ins can notify the driver of a modified user interface option. |
| [IPrintCoreUI2::DrvUpgradeRegistrySetting](nf-prcomoem-iprintcoreui2-drvupgraderegistrysetting.md) | The IPrintCoreUI2::DrvUpgradeRegistrySetting method is provided by the Windows XP Pscript5 driver so that Pscript5 user interface plug-ins can update device settings stored in the registry. |
| [IPrintCoreUI2::EnumConstrainedOptions](nf-prcomoem-iprintcoreui2-enumconstrainedoptions.md) | The IPrintCoreUI2::EnumConstrainedOptions method determines which options of a feature are constrained. |
| [IPrintCoreUI2::EnumFeatures](nf-prcomoem-iprintcoreui2-enumfeatures.md) | The IPrintCoreUI2::EnumFeatures method enumerates a printer's available features. |
| [IPrintCoreUI2::EnumOptions](nf-prcomoem-iprintcoreui2-enumoptions.md) | The IPrintCoreUI2::EnumOptions method enumerates the available options of a specific feature. |
| [IPrintCoreUI2::GetFeatureAttribute](nf-prcomoem-iprintcoreui2-getfeatureattribute.md) | The IPrintCoreUI2::GetFeatureAttribute method retrieves the feature attribute list or the value of a specific feature attribute. |
| [IPrintCoreUI2::GetGlobalAttribute](nf-prcomoem-iprintcoreui2-getglobalattribute.md) | The IPrintCoreUI2::GetGlobalAttribute method retrieves the global attribute list or the value of a specific global attribute. |
| [IPrintCoreUI2::GetOptionAttribute](nf-prcomoem-iprintcoreui2-getoptionattribute.md) | The IPrintCoreUI2::GetOptionAttribute method retrieves the option attribute list or the value of a specific option attribute. |
| [IPrintCoreUI2::GetOptions](nf-prcomoem-iprintcoreui2-getoptions.md) | The IPrintCoreUI2::GetOptions method retrieves the driver's current feature settings in the format of a list of feature/option keyword pairs. |
| [IPrintCoreUI2::QuerySimulationSupport](nf-prcomoem-iprintcoreui2-querysimulationsupport.md) | The IPrintCoreUI2::QuerySimulationSupport method retrieves a spooler simulation capability structure, which indicates the kinds of simulation the spooler supports. |
| [IPrintCoreUI2::SetOptions](nf-prcomoem-iprintcoreui2-setoptions.md) | The IPrintCoreUI2::SetOptions method sets the driver's feature settings. |
| [IPrintCoreUI2::WhyConstrained](nf-prcomoem-iprintcoreui2-whyconstrained.md) | The IPrintCoreUI2::WhyConstrained method determines why the specified feature/option selection is constrained. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | prcomoem.h |
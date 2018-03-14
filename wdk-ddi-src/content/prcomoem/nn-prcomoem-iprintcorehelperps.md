---
UID: NN:prcomoem.IPrintCoreHelperPS
title: IPrintCoreHelperPS
author: windows-driver-content
description: This section describes the methods that are defined for the IPrintCoreHelperPS COM interface.
old-location: print\iprintcorehelperps_interface.htm
old-project: print
ms.assetid: 2be594f1-1eb1-42e0-a345-ee7edf4d96dd
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintCoreHelperPS, IPrintCoreHelperPS interface [Print Devices], IPrintCoreHelperPS interface [Print Devices], described, prcomoem/IPrintCoreHelperPS, print.iprintcorehelperps_interface, print_unidrv-pscript_allplugins_793ff9db-3ae7-4c10-a84e-bc974a72529e.xml
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
req.lib: 
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
-	IPrintCoreHelperPS
product: Windows
targetos: Windows
req.typenames: OEMPTOPTS, *POEMPTOPTS
req.product: Windows 10 or later.
---

# IPrintCoreHelperPS interface

This section describes the methods that are defined for the <b>IPrintCoreHelperPS</b> COM interface.

## Methods

<p>The <b>IPrintCoreHelperPS</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintCoreHelperPS::CreateInstanceOfMSXMLObject](nf-prcomoem-iprintcorehelperps-createinstanceofmsxmlobject.md) | The IPrintCoreHelperPS::CreateInstanceOfMSXMLObject method creates an instance of an MSXML object. |
| [IPrintCoreHelperPS::EnumConstrainedOptions](nf-prcomoem-iprintcorehelperps-enumconstrainedoptions.md) | The IPrintCoreHelperPS::EnumConstrainedOptions method provides a list of all of the options that are constrained in a particular feature, based on current settings. |
| [IPrintCoreHelperPS::EnumFeatures](nf-prcomoem-iprintcorehelperps-enumfeatures.md) | The IPrintCoreHelperPS::EnumFeatures method gets a list of all available features, including synthesized and core driver-implement features. |
| [IPrintCoreHelperPS::EnumOptions](nf-prcomoem-iprintcorehelperps-enumoptions.md) | The IPrintCoreHelperPS::EnumOptions method gets a list of available options for the given feature. |
| [IPrintCoreHelperPS::GetFeatureAttribute](nf-prcomoem-iprintcorehelperps-getfeatureattribute.md) | The IPrintCoreHelperPS::GetFeatureAttribute method retrieves the feature attribute list or the value of a specific feature attribute. |
| [IPrintCoreHelperPS::GetFontSubstitution](nf-prcomoem-iprintcorehelperps-getfontsubstitution.md) | The IPrintCoreHelperPS::GetFontSubstitution method indicates which device font, if any, is used as a substitution font for a specified TrueType font. |
| [IPrintCoreHelperPS::GetGlobalAttribute](nf-prcomoem-iprintcorehelperps-getglobalattribute.md) | The IPrintCoreHelperPS::GetGlobalAttribute method retrieves the global attribute list or the value of a specific global attribute. |
| [IPrintCoreHelperPS::GetOption](nf-prcomoem-iprintcorehelperps-getoption.md) | The IPrintCoreHelperPS::GetOption method gets a specified option for a given feature. |
| [IPrintCoreHelperPS::GetOptionAttribute](nf-prcomoem-iprintcorehelperps-getoptionattribute.md) | The IPrintCoreHelperPS::GetOptionAttribute method retrieves the option attribute list or the value of a specific option attribute. |
| [IPrintCoreHelperPS::SetFontSubstitution](nf-prcomoem-iprintcorehelperps-setfontsubstitution.md) | The IPrintCoreHelperPS::SetFontSubstitution method specifies the device font to print in place of a given TrueType font. |
| [IPrintCoreHelperPS::SetOptions](nf-prcomoem-iprintcorehelperps-setoptions.md) | The IPrintCoreHelperPS::SetOptions method sets multiple feature-option pairs at the same time. |
| [IPrintCoreHelperPS::WhyConstrained](nf-prcomoem-iprintcorehelperps-whyconstrained.md) | The IPrintCoreHelperPS::WhyConstrained method provides a list of options that constrain the specified feature-option pair in the current configuration. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | prcomoem.h |
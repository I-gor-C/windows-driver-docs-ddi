---
UID: NF.prcomoem.IPrintOemUI.DeviceCapabilities
title: IPrintOemUI::DeviceCapabilities
author: windows-driver-content
description: The IPrintOemUI::DeviceCapabilities method enables a user interface plug-in to specify customized device capabilities.
old-location: print\iprintoemui_devicecapabilities.htm
ms.assetid: a3d3e986-41ab-489a-a930-b10e9989553f
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: prcomoem.h
req.include-header: Prcomoem.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintOemUI.DeviceCapabilities
req.alt-loc: prcomoem.h
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
ms.keywords: IPrintOemUI, DeviceCapabilities, IPrintOemUI::DeviceCapabilities
req.iface: IPrintOemUI
req.product: Windows 10 or later.
---

# IPrintOemUI::DeviceCapabilities method



## -description
<p>The <code>IPrintOemUI::DeviceCapabilities</code> method enables a user interface plug-in to specify customized device capabilities.</p>


## -syntax

````
HRESULT DeviceCapabilities(
   POEMUIOBJ poemuiobj,
   HANDLE    hPrinter,
   PWSTR     pDeviceName,
   WORD      wCapability,
   PVOID     pOutput,
   PDEVMODE  pPublicDM,
   PVOID     pOEMDM,
   DWORD     dwOld,
   DWORD     *dwResult
);
````


## -parameters
<dl>

### -param <i>poemuiobj</i> 

<dd>
<p>Caller-supplied pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559571">OEMUIOBJ</a> structure.</p>
</dd>

### -param <i>hPrinter</i> 

<dd>
<p>Caller-supplied handle to the printer device.</p>
</dd>

### -param <i>pDeviceName</i> 

<dd>
<p>Caller-supplied pointer to a string representing the device name.</p>
</dd>

### -param <i>wCapability</i> 

<dd>
<p>Caller-supplied flag indicating the type of information the method should return. For a list of flags, see the description of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548539">DrvDeviceCapabilities</a> function.</p>
</dd>

### -param <i>pOutput</i> 

<dd>
<p>Caller-supplied pointer to a buffer to receive the requested information. The type of information returned is dependent on the flag specified by <i>wCapability</i>.</p>
</dd>

### -param <i>pPublicDM</i> 

<dd>
<p>Caller-supplied pointer to a validated <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure.</p>
</dd>

### -param <i>pOEMDM</i> 

<dd>
<p>Caller-supplied pointer to the user interface plug-in's private DEVMODEW structure members.</p>
</dd>

### -param <i>dwOld</i> 

<dd>
<p>Caller-supplied return value from the printer driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff548539">DrvDeviceCapabilities</a> function, or from another user interface plug-in. For more information, see the following Remarks section.</p>
</dd>

### -param <i>dwResult</i> 

<dd>
<p>A return value that is dependent on the flag specified by <i>wCapability</i>. For more information, see the description of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548539">DrvDeviceCapabilities</a> function and the following Remarks section.</p>
</dd>
</dl>

## -returns
<p>The method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation succeeded.</p><dl>
<dt><b>S_DEVCAP_OUTPUT_FULL_REPLACEMENT</b></dt>
</dl><p>The plug-in intends to use the buffer that is pointed to by the <i>pOutput</i> parameter for its own purposes. This return value is defined in prcomoem.h. For more information about when to use this return value, see the following Remarks section.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The operation failed.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The method is not implemented.</p>

<p> </p>

## -remarks
<p>A user interface plug-in's <code>IPrintOemUI::DeviceCapabilities</code> method performs the same types of operations as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548539">DrvDeviceCapabilities</a> function that is exported by user-mode printer interface DLLs. The method specifies capabilities provided by the printer.</p>

<p>You can use the <code>IPrintOemUI::DeviceCapabilities</code> method to preempt Unidrv support for a capability, or to add a capability that the printer driver doesn't provide. The driver calls <code>IPrintOemUI::DeviceCapabilities</code> from within its <a href="https://msdn.microsoft.com/library/windows/hardware/ff548539">DrvDeviceCapabilities</a> function.</p>

<p>If the <code>IPrintOemUI::DeviceCapabilities</code> method indicates customized support for a capability (by setting appropriate bits in response to a received DC_FIELDS flag), customized code must completely support the capability. Complete support typically includes returning information about the capability in response to calls to the <code>IPrintOemUI::DeviceCapabilities</code> method, plus providing appropriate user-mode or kernel-mode code to implement the capability.</p>

<p>If <code>IPrintOemUI::DeviceCapabilities</code> methods are exported by multiple user interface plug-ins, the methods are called in the order that the plug-ins are specified for installation. Each time a plug-in's <code>IPrintOemUI::DeviceCapabilities</code> method is called, its <i>dwOld</i> input value is the return value from the previously called plug-in's <code>IPrintOemUI::DeviceCapabilities</code> method. For the first plug-in called, <i>dwOld</i> contains the return value from the printer driver's <b>DrvDeviceCapabilities</b> function. Likewise, the buffer pointed to by <i>pOutput</i> contains, on input, any contents placed there by a previously called <code>IPrintOemUI::DeviceCapabilities</code> method or <b>DrvDeviceCapabilities</b> function.</p>

<p>For multiple user interface plug-ins to work in conjunction with each other, each <code>IPrintOemUI::DeviceCapabilities</code> method must obey the following rules:</p>

<p>If a user interface plug-in does not support a specified capability, its <code>IPrintOemUI::DeviceCapabilities</code> method should just return the contents of the <i>dwOld</i> parameter in <i>dwResult</i>.</p>

<p>If a user interface plug-in supports the capability, its <code>IPrintOemUI::DeviceCapabilities</code> method should ignore <i>dwOld</i> and the contents of the buffer pointed to by <i>pOutput</i>. It should provide a return value and buffer contents appropriate for indicating that it supports the specified capability. If the method detects an error, it should return GDI_ERROR in <i>dwResult</i>.</p>

<p>If you want a user interface plug-in to modify the capabilities information received in the buffer pointed to by <i>pOutput</i>, its <code>IPrintOemUI::DeviceCapabilities</code> method should modify the buffer contents and return an appropriate return value in <i>dwResult</i>. For example, if <i>wCapability</i> is DC_FIELDS, the method should OR the bits it needs to set with the bits that are set in <i>dwOld</i>, and return the result of the OR operation in <i>dwResult</i>.</p>

<p>The preceding rules should be followed even if the received contents of <i>dwOld</i> is GDI_ERROR.</p>

<p>When the driver's <b>DrvDeviceCapabilities</b> function is called with the DC_FIELDS flag set, the function calls all <code>IPrintOemUI::DeviceCapabilities</code> methods, also specifying DC_FIELDS, and returns the union of all set bits to the caller.</p>

<p>The S_DEVCAP_OUTPUT_FULL_REPLACEMENT return value is new in Windows Vista, and applies to both Unidrv and Pscript5 user interface plug-ins. A plug-in should use the S_DEVCAP_OUTPUT_FULL_REPLACEMENT return value only if it requires complete control over what is placed in the buffer that is pointed to by the <i>pOutput</i> parameter. Neither the Unidrv nor the Pscript5 core driver will place data in the <i>pOutput</i> buffer when the plug-in returns S_DEVCAP_OUTPUT_FULL_REPLACEMENT. A plug-in might need to return this value when a setting in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure (which is pointed to by the <i>pPublicDM</i> and <i>pOEMDM</i> parameters) indicates to the user interface plug-in that it should report device capability data that is different from that specified in the GPD or PPD file. For example, a DEVMODEW structure that specifies photo printing might require a different set of paper types than those that are specified in the GPD or PPD file. In such a situation, and regardless of the values of the <i>pOutput</i> and <i>dwOld</i> parameters, the plug-in should return S_DEVCAP_OUTPUT_FULL_REPLACEMENT, and should set the <i>dwResult</i> parameter to the number of paper types that it intends to report. If <i>pOutput</i> is not <b>NULL</b>, the plug-in should also fill the buffer that is pointed to by <i>pOutput</i> with the desired set of paper types, and should set <i>dwResult</i> to the number of paper types that the plug-in intends to report. </p>

<p>When multiple user interface plug-ins are active at the same time, and one of them returns S_DEVCAP_OUTPUT_FULL_REPLACEMENT, the Unidrv or Pscript5 core driver interprets this return value to mean that the plug-ins intend to provide full replacement output data. As a result, the core driver does not place any data into the <i>pOutput</i> buffer before it calls the plug-ins. (The core driver calls the plug-ins in the same order that was specified for their installation.)</p>

<p>In situations where the values that the core driver places in the <i>pOutput</i> buffer do not need to be replaced, the plug-in should return S_OK. The Unidrv and Pscript5 core drivers recognize the S_DEVCAP_OUTPUT_FULL_REPLACEMENT return value only for device capabilities that use the <i>pOutput</i> buffer--in other words, when the <i>wCapability</i> parameter is set to one of the following flags:</p><dl>
<dd>
<p>DC_PAPERNAMES</p>
</dd>
<dd>
<p>DC_PAPERS</p>
</dd>
<dd>
<p>DC_PAPERSIZE</p>
</dd>
<dd>
<p>DC_BINNAMES</p>
</dd>
<dd>
<p>DC_BINS</p>
</dd>
<dd>
<p>DC_NUP</p>
</dd>
<dd>
<p>DC_PERSONALITY</p>
</dd>
<dd>
<p>DC_MEDIAREADY</p>
</dd>
<dd>
<p>DC_MEDIATYPENAMES</p>
</dd>
<dd>
<p>DC_MEDIATYPES</p>
</dd>
<dd>
<p>DC_ENUMRESOLUTIONS</p>
</dd>
</dl><p>DC_PAPERNAMES</p>

<p>DC_PAPERS</p>

<p>DC_PAPERSIZE</p>

<p>DC_BINNAMES</p>

<p>DC_BINS</p>

<p>DC_NUP</p>

<p>DC_PERSONALITY</p>

<p>DC_MEDIAREADY</p>

<p>DC_MEDIATYPENAMES</p>

<p>DC_MEDIATYPES</p>

<p>DC_ENUMRESOLUTIONS</p>

<p>For more information about creating and installing user interface plug-ins, see <a href="NULL">Customizing Microsoft's Printer Drivers</a>.</p>

<p>A user interface plug-in's <code>IPrintOemUI::DeviceCapabilities</code> method performs the same types of operations as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548539">DrvDeviceCapabilities</a> function that is exported by user-mode printer interface DLLs. The method specifies capabilities provided by the printer.</p>

<p>You can use the <code>IPrintOemUI::DeviceCapabilities</code> method to preempt Unidrv support for a capability, or to add a capability that the printer driver doesn't provide. The driver calls <code>IPrintOemUI::DeviceCapabilities</code> from within its <a href="https://msdn.microsoft.com/library/windows/hardware/ff548539">DrvDeviceCapabilities</a> function.</p>

<p>If the <code>IPrintOemUI::DeviceCapabilities</code> method indicates customized support for a capability (by setting appropriate bits in response to a received DC_FIELDS flag), customized code must completely support the capability. Complete support typically includes returning information about the capability in response to calls to the <code>IPrintOemUI::DeviceCapabilities</code> method, plus providing appropriate user-mode or kernel-mode code to implement the capability.</p>

<p>If <code>IPrintOemUI::DeviceCapabilities</code> methods are exported by multiple user interface plug-ins, the methods are called in the order that the plug-ins are specified for installation. Each time a plug-in's <code>IPrintOemUI::DeviceCapabilities</code> method is called, its <i>dwOld</i> input value is the return value from the previously called plug-in's <code>IPrintOemUI::DeviceCapabilities</code> method. For the first plug-in called, <i>dwOld</i> contains the return value from the printer driver's <b>DrvDeviceCapabilities</b> function. Likewise, the buffer pointed to by <i>pOutput</i> contains, on input, any contents placed there by a previously called <code>IPrintOemUI::DeviceCapabilities</code> method or <b>DrvDeviceCapabilities</b> function.</p>

<p>For multiple user interface plug-ins to work in conjunction with each other, each <code>IPrintOemUI::DeviceCapabilities</code> method must obey the following rules:</p>

<p>If a user interface plug-in does not support a specified capability, its <code>IPrintOemUI::DeviceCapabilities</code> method should just return the contents of the <i>dwOld</i> parameter in <i>dwResult</i>.</p>

<p>If a user interface plug-in supports the capability, its <code>IPrintOemUI::DeviceCapabilities</code> method should ignore <i>dwOld</i> and the contents of the buffer pointed to by <i>pOutput</i>. It should provide a return value and buffer contents appropriate for indicating that it supports the specified capability. If the method detects an error, it should return GDI_ERROR in <i>dwResult</i>.</p>

<p>If you want a user interface plug-in to modify the capabilities information received in the buffer pointed to by <i>pOutput</i>, its <code>IPrintOemUI::DeviceCapabilities</code> method should modify the buffer contents and return an appropriate return value in <i>dwResult</i>. For example, if <i>wCapability</i> is DC_FIELDS, the method should OR the bits it needs to set with the bits that are set in <i>dwOld</i>, and return the result of the OR operation in <i>dwResult</i>.</p>

<p>The preceding rules should be followed even if the received contents of <i>dwOld</i> is GDI_ERROR.</p>

<p>When the driver's <b>DrvDeviceCapabilities</b> function is called with the DC_FIELDS flag set, the function calls all <code>IPrintOemUI::DeviceCapabilities</code> methods, also specifying DC_FIELDS, and returns the union of all set bits to the caller.</p>

<p>The S_DEVCAP_OUTPUT_FULL_REPLACEMENT return value is new in Windows Vista, and applies to both Unidrv and Pscript5 user interface plug-ins. A plug-in should use the S_DEVCAP_OUTPUT_FULL_REPLACEMENT return value only if it requires complete control over what is placed in the buffer that is pointed to by the <i>pOutput</i> parameter. Neither the Unidrv nor the Pscript5 core driver will place data in the <i>pOutput</i> buffer when the plug-in returns S_DEVCAP_OUTPUT_FULL_REPLACEMENT. A plug-in might need to return this value when a setting in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure (which is pointed to by the <i>pPublicDM</i> and <i>pOEMDM</i> parameters) indicates to the user interface plug-in that it should report device capability data that is different from that specified in the GPD or PPD file. For example, a DEVMODEW structure that specifies photo printing might require a different set of paper types than those that are specified in the GPD or PPD file. In such a situation, and regardless of the values of the <i>pOutput</i> and <i>dwOld</i> parameters, the plug-in should return S_DEVCAP_OUTPUT_FULL_REPLACEMENT, and should set the <i>dwResult</i> parameter to the number of paper types that it intends to report. If <i>pOutput</i> is not <b>NULL</b>, the plug-in should also fill the buffer that is pointed to by <i>pOutput</i> with the desired set of paper types, and should set <i>dwResult</i> to the number of paper types that the plug-in intends to report. </p>

<p>When multiple user interface plug-ins are active at the same time, and one of them returns S_DEVCAP_OUTPUT_FULL_REPLACEMENT, the Unidrv or Pscript5 core driver interprets this return value to mean that the plug-ins intend to provide full replacement output data. As a result, the core driver does not place any data into the <i>pOutput</i> buffer before it calls the plug-ins. (The core driver calls the plug-ins in the same order that was specified for their installation.)</p>

<p>In situations where the values that the core driver places in the <i>pOutput</i> buffer do not need to be replaced, the plug-in should return S_OK. The Unidrv and Pscript5 core drivers recognize the S_DEVCAP_OUTPUT_FULL_REPLACEMENT return value only for device capabilities that use the <i>pOutput</i> buffer--in other words, when the <i>wCapability</i> parameter is set to one of the following flags:</p><dl>
<dd>
<p>DC_PAPERNAMES</p>
</dd>
<dd>
<p>DC_PAPERS</p>
</dd>
<dd>
<p>DC_PAPERSIZE</p>
</dd>
<dd>
<p>DC_BINNAMES</p>
</dd>
<dd>
<p>DC_BINS</p>
</dd>
<dd>
<p>DC_NUP</p>
</dd>
<dd>
<p>DC_PERSONALITY</p>
</dd>
<dd>
<p>DC_MEDIAREADY</p>
</dd>
<dd>
<p>DC_MEDIATYPENAMES</p>
</dd>
<dd>
<p>DC_MEDIATYPES</p>
</dd>
<dd>
<p>DC_ENUMRESOLUTIONS</p>
</dd>
</dl><p>DC_PAPERNAMES</p>

<p>DC_PAPERS</p>

<p>DC_PAPERSIZE</p>

<p>DC_BINNAMES</p>

<p>DC_BINS</p>

<p>DC_NUP</p>

<p>DC_PERSONALITY</p>

<p>DC_MEDIAREADY</p>

<p>DC_MEDIATYPENAMES</p>

<p>DC_MEDIATYPES</p>

<p>DC_ENUMRESOLUTIONS</p>

<p>For more information about creating and installing user interface plug-ins, see <a href="NULL">Customizing Microsoft's Printer Drivers</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Prcomoem.h (include Prcomoem.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548539">DrvDeviceCapabilities</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemUI::DeviceCapabilities method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

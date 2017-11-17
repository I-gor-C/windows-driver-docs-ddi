# Declarations in the wdfverifier header
This header Wdfverifier contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [*PFN_WDFVERIFIERKEBUGCHECK callback function](nc-wdfverifier-pfn-wdfverifierkebugcheck.md) | TBD |
| [*PFN_WDFGETTRIAGEINFO callback function](nc-wdfverifier-pfn-wdfgettriageinfo.md) | TBD |
| [*PFN_WDFVERIFIERDBGBREAKPOINT callback function](nc-wdfverifier-pfn-wdfverifierdbgbreakpoint.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfGetTriageInfo function](nf-wdfverifier-wdfgettriageinfo.md) | The WdfGetTriageInfo method is reserved for internal use only. |
| [WdfVerifierKeBugCheck function](nf-wdfverifier-wdfverifierkebugcheck.md) | The WdfVerifierKeBugCheck function creates a bug check. |
| [WdfVerifierDbgBreakPoint function](nf-wdfverifier-wdfverifierdbgbreakpoint.md) | The WdfVerifierDbgBreakPoint function breaks into a kernel debugger, if a debugger is running. |

This header is used in these topics:

- [wdf](..content/_wdf)
